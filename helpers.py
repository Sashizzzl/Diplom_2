import random

class SignUpData:
    unique_user_data = {"email": f'new_user_{random.randint(1000, 9999)}@gmail.com',
                   "password": random.randint(10000, 99999), "name": f'Sasha{random.randint(1000, 9999)}'}
    double_sign_in = {"email": f'new_user_{random.randint(100, 999)}@gmail.com',
                   "password": random.randint(1000, 9999), "name": f'Sasha{random.randint(100, 999)}'}
    user_data_no_email = {"email": '',
                   "password": random.randint(10000, 99999), "name": f'Sasha{random.randint(1000, 9999)}'}
    user_data_no_password = {"email": f'new_user_{random.randint(1000, 9999)}@gmail.com',
                   "password": '', "name": f'Sasha{random.randint(1000, 9999)}'}
    user_data_no_name = {"email": f'new_user_{random.randint(1000, 9999)}@gmail.com',
                   "password": random.randint(10000, 99999), "name": ''}
class LoginData:
    incorrect_email_and_password = {"email": f'new_user_{random.randint(1000, 9999)}@gmail.com',
                   "password": random.randint(10000, 99999), "name": f'Sasha{random.randint(1000, 9999)}'}
class ChangeUserData:
    email = {"email": f'new_user_{random.randint(1000, 9999)}@gmail.com'}
    name = {"name": f'Sasha{random.randint(1000, 9999)}'}
class Ingredients:
    correct_id = '61c0c5a71d1f82001bdaaa6d'
    incorrect_id = random.randint(100,999)
