import requests
import allure
from endpoints.base_api import BaseAPI


class GetUser(BaseAPI):
    endpoint = '/get_user/'

    @allure.step("Получить пользователя по ID")
    def get_user_by_id(self, user_id, headers=None):
        """Получает пользователя по ID"""
        if headers is None:
            headers = {}

        self.response = requests.get(
            self.base_url + self.endpoint + str(user_id),
            headers=headers
        )
        self.response_json = self.response.json()

    @allure.step("Проверить наличие ключей 'avatar_url', 'email', 'id', 'name', 'role', 'username' в теле ответа")
    def check_user_keys(self):
        """Проверяет наличие всех нужных ключей в ответе"""
        if not self.response_json:
            return False, "Response JSON is empty"

        if 'user' not in self.response_json:
            return False, "Missing 'user' key"

        user_data = self.response_json['user']
        expected_keys = ['avatar_url', 'email', 'id', 'name', 'role', 'username']

        missing_keys = []
        for key in expected_keys:
            if key not in user_data:
                missing_keys.append(key)

        if missing_keys:
            return False, f"Missing keys: {missing_keys}"

        return True, "All keys present"

    @allure.step("Проверить что данные полученного пользователя совпадают с данными созданного")
    def verify_user_data(self, expected_data, user_id):
        """
        Проверяет что данные пользователя совпадают с ожидаемыми
        expected_data: словарь с данными из payload создания пользователя
        user_id: ID пользователя для проверки
        """
        if not self.response_json or 'user' not in self.response_json:
            return False, "Invalid response structure"

        user_data = self.response_json['user']

        # Проверяем совпадение данных
        fields_to_check = [
            ('email', expected_data['email']),
            ('name', expected_data['name']),
            ('username', expected_data['username']),
            ('role', expected_data['role']),
            ('avatar_url', expected_data['avatar_url'])
        ]

        errors = []

        # Проверяем ID
        if user_data.get('id') != user_id:
            errors.append(f"ID mismatch: expected {user_id}, got {user_data.get('id')}")

        # Проверяем остальные поля
        for field_name, expected_value in fields_to_check:
            actual_value = user_data.get(field_name)
            if actual_value != expected_value:
                errors.append(f"{field_name}: expected '{expected_value}', got '{actual_value}'")

        if errors:
            return False, errors

        return True, "All data matches"

    @allure.step("Проверить сообщение: 'Пользователь не найден'")
    def check_message(self):
        """Проверяет сообщение в ответе"""
        if self.response_json and 'message' in self.response_json:
            return self.response_json['message'] == "Пользователь не найден"
        return False