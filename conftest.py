import pytest
# from tests.api.ships_api import ShipsAPI
#
# @pytest.fixture
# def ships_api():
#     return ShipsAPI()
#
# @pytest.fixture
# def authorization():
#     """Фикстура для обратной совместимости"""
#     api = ShipsAPI()
#     return api.headers
#
# @pytest.fixture
# def sample_ship_data():
#     return {
#         "corporation_id": 1192,
#         "custom_photo_url": "http://example.com/enterprise.jpg",
#         "description": "Новый корабль",
#         "name": "Молния",
#         "type_id": 3
#     }
#
#
# @pytest.fixture
# def created_ship_id(ships_api, sample_ship_data):
#     """Фикстура создает корабль и возвращает его ID, затем удаляет"""
#     response = ships_api.create_ship(sample_ship_data)
#     assert response.status_code == 201
#     ship_id = response.json()["ship_id"]
#     yield ship_id  # Передаем ID в тест
#     # Удаляем после теста
#     ships_api.delete_ship(ship_id)