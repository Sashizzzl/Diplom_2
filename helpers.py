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
    password = {"password": random.randint(100000, 999999)}
class Ingredients:
    correct_id = '61c0c5a71d1f82001bdaaa6d'
    incorrect_id = random.randint(100,999)
class Answers:
    need_authorization_text = '{"success":false,"message":"You should be authorised"}'
    success_text = '"success":true'
    need_ids_text = '{"success":false,"message":"Ingredient ids must be provided"}'
    server_error_text = 'Server Error'
    logout_text = '{"success":true,"message":"Successful logout"}'
    incorrect_data_text = '{"success":false,"message":"email or password are incorrect"}'
    already_exists_text = '{"success":false,"message":"User already exists"}'
    not_enough_data_text = '{"success":false,"message":"Email, password and name are required fields"}'

