import allure
import requests


class BaseAPI:
    base_url = 'https://api.brainy.run/go'
    endpoint: str
    response: requests.Response

    @allure.step("Проверить статус код ответа")
    def check_status_is_(self, status):
        return self.response.status_code == status