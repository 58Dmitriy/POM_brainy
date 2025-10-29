import requests
import allure
from endpoints.base_api import BaseAPI


class DeleteUser(BaseAPI):
    endpoint = '/delete_user/'

    @allure.step("Удалить пользователя по ID")
    def delete_user_by_id(self, user_id, headers=None):
        """Удаляет пользователя по ID"""
        if headers is None:
            headers = {}

        self.response = requests.delete(
            self.base_url + self.endpoint + str(user_id),
            headers=headers
        )
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = None

    @allure.step("Проверить сообщение: 'Пользователь успешно удален'")
    def check_message(self):
        """Проверяет сообщение в ответе"""
        if self.response_json and 'message' in self.response_json:
            return self.response_json['message'] == "Пользователь успешно удален"
        return False