import requests
import base64
import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def authorization():
    # Получаем учетные данные из переменных окружения
    student_login = os.getenv('STUDENT_LOGIN')
    student_password = os.getenv('STUDENT_PASSWORD')
    # Кодируем логин и пароль в base64 для Basic Auth
    credentials = f"{student_login}:{student_password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
            }
    return headers


@pytest.fixture
def ship_id_for_delete_ship(authorization):
    payload = {

        "corporation_id": 1192,
        "custom_photo_url": "http://example.com/enterprise.jpg",
        "description": "Новый корабль",
        "name": "Молния",
        "type_id": 3

    }

    response = requests.post('https://api.brainy.run/go/add_ship', headers=authorization, json=payload)
    assert response.status_code == 201, f"Не удалось создать корабль: {response.text}"

    data = response.json()
    return data['ship_id']  # Просто возвращаем ID

@pytest.fixture
def ship_id_for_get(authorization):
    payload = {

        "corporation_id": 1192,
        "custom_photo_url": "http://example.com/enterprise.jpg",
        "description": "Новый корабль",
        "name": "Молния",
        "type_id": 3

    }

    response = requests.post('https://api.brainy.run/go/add_ship', headers=authorization, json=payload)
    assert response.status_code == 201, f"Не удалось создать корабль: {response.text}"

    data = response.json()
    created_ship_id = data['ship_id']  # Сохраняем ID в переменную
    yield created_ship_id  # Сохраняем ID в переменную
    requests.delete(f'https://api.brainy.run/go/delete_ship/{created_ship_id}', headers=authorization)

def test_get_all_ships_typs(authorization):
    response = requests.get('https://api.brainy.run/go/get_ship_types', headers=authorization)
    assert response.status_code == 200

def test_get_ships_by_owner_corporation(authorization, ship_id_for_get):
    corporation_id = 1192
    response = requests.get(f'https://api.brainy.run/go/get_ships/{corporation_id}', headers=authorization)
    assert response.status_code == 200
    data = response.json()
    # Извлекаем все ID кораблей
    ship_ids = [ship['id'] for ship in data['ships']]
    print("Все ID кораблей:", ship_ids)

def test_add_new_ship(authorization):

    payload = {

        "corporation_id": 1192,
        "custom_photo_url": "http://example.com/enterprise.jpg",
        "description": "Новый корабль",
        "name": "Молния",
        "type_id": 3

    }

    response = requests.post('https://api.brainy.run/go/add_ship', headers=authorization, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "ship_id" in data
    print(f"Корабль создан с ID: {data['ship_id']}")

def test_delete_ship(authorization, ship_id_for_delete_ship):

    response = requests.delete(f'https://api.brainy.run/go/delete_ship/{ship_id_for_delete_ship}', headers=authorization)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Корабль успешно удален"
    response = requests.get(f'https://api.brainy.run/go/get_ships/1192', headers=authorization)
    assert response.status_code == 204
