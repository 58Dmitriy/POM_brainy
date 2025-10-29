import random
import string

class UserData:

    @staticmethod
    def get_create_user_payload():
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        roles = ['owner', 'employee', 'passenger']
        names = [
            'Александр', 'Алексей', 'Анастасия', 'Анна', 'Артем', 'Вадим', 'Валерия',
            'Виктория', 'Владимир', 'Галина', 'Дарья', 'Денис', 'Евгений', 'Екатерина',
            'Иван', 'Ирина', 'Кирилл', 'Мария', 'Максим', 'Наталья', 'Олег', 'Ольга',
            'Павел', 'Сергей', 'Татьяна', 'Юлия', 'Яна'
        ]
        random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return {
            "avatar_url": "https://brainy.run/wp-content/uploads/2024/05/candidate2.png",
            "email": f"{random_string}@brainy.run",
            "name": random.choice(names),
            "password": random_password,
            "role": random.choice(roles),
            "username": random_string
        }