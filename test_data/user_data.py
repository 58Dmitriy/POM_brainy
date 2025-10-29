import random
import string

class UserData:

    @staticmethod
    def get_create_user_payload():
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return {
            "avatar_url": "https://brainy.run/wp-content/uploads/2024/05/candidate2.png",
            "email": f"user_{random_string}@brainy.run",
            "name": "Брейни",
            "password": "superpassword",
            "role": "user",
            "username": f"user_{random_string}"
        }