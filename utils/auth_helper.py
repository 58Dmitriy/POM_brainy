import os
import base64
from dotenv import load_dotenv

load_dotenv()


def get_auth_headers():
    """Функция для получения headers авторизации"""
    student_login = os.getenv('STUDENT_LOGIN')
    student_password = os.getenv('STUDENT_PASSWORD')
    credentials = f"{student_login}:{student_password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
    }
    return headers