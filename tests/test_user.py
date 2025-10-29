import pytest
from endpoints.user.create_user import CreateUser
from endpoints.user.delete_user import DeleteUser
from endpoints.user.get_user import GetUser
from utils.auth_helper import get_auth_headers
import allure
from test_data.user_data import UserData

@allure.title("Тест создания и удаления пользователя")
def test_create_and_delete_user():
    """Тест создания и удаления пользователя"""
    # Получаем headers для авторизации
    headers = get_auth_headers()

    # Получаем данные для создания пользователя
    payload = UserData.get_create_user_payload()

    # Создаем экземпляр класса и выполняем запрос
    create_user = CreateUser()
    create_user.create_new_user(payload=payload, headers=headers)

    # Проверки создания
    assert create_user.check_status_is_(201)
    assert create_user.check_message()

    # Получаем ID созданного пользователя
    user_id = create_user.response_json.get('user_id')
    assert user_id is not None, "User ID not found in response"

    # Удаляем пользователя
    delete_user = DeleteUser()
    delete_user.delete_user_by_id(user_id=user_id, headers=headers)

    # Проверки удаления
    assert delete_user.check_status_is_(200)
    assert delete_user.check_message()

@allure.title("Тест на получение пользователя")
def test_get_user():
    """Тест на получение пользователя"""
    headers = get_auth_headers()
    get_user = GetUser()
    get_user.get_user_by_id(1,headers=headers)
    print(get_user.response_json)
    assert get_user.check_status_is_(200)
    assert get_user.check_user_keys()

@allure.title("Тест на создание, получение и удаление пользователя")
def test_create_get_and_delete_user():
    """Комбинированный тест: создание, получение и удаление пользователя"""
    headers = get_auth_headers()
    create_user = CreateUser()
    payload = UserData.get_create_user_payload()
    create_user.create_new_user(payload=payload, headers=headers)
    assert create_user.check_status_is_(201)
    assert create_user.check_message()
    user_id = create_user.response_json.get('user_id')
    assert user_id is not None, "User ID not found in response"
    get_user = GetUser()
    get_user.get_user_by_id(user_id=user_id, headers=headers)
    assert get_user.check_status_is_(200)
    assert get_user.verify_user_data(payload, user_id)
    delete_user = DeleteUser()
    delete_user.delete_user_by_id(user_id=user_id, headers=headers)
    get_user.get_user_by_id(user_id=user_id, headers=headers)
    assert get_user.check_status_is_(404)
    assert get_user.check_message()




