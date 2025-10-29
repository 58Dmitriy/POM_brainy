import requests
import allure
from endpoints.base_api import BaseAPI

class CreateUser(BaseAPI):
    endpoint = '/create_user'

    @allure.step("Создать нового пользователя")
    def create_new_user(self, payload, headers=None):
        if headers is None:
            headers = {}

        self.response = requests.post(
            self.base_url + self.endpoint,
            json=payload,
            headers=headers
        )
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = None

    @allure.step("Проверить сообщение: 'Пользователь успешно создан'")
    def check_message(self):
        """Проверяет сообщение в ответе"""
        if self.response_json and 'message' in self.response_json:
            return self.response_json['message'] == "Пользователь успешно создан"
        return False