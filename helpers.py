import random

class SignUpData:
    unique_user_data = {"email": f'new_user_{random.randint(1000, 9999)}@gmail.com',
                   "password": random.randint(10000, 99999), "name": f'Sasha{random.randint(1000, 9999)}'}
    user_data_no_email = {"email": '',
                   "password": random.randint(10000, 99999), "name": f'Sasha{random.randint(1000, 9999)}'}
    user_data_no_password = {"email": f'new_user_{random.randint(1000, 9999)}@gmail.com',
                   "password": '', "name": f'Sasha{random.randint(1000, 9999)}'}
    user_data_no_name = {"email": f'new_user_{random.randint(1000, 9999)}@gmail.com',
                   "password": random.randint(10000, 99999), "name": ''}