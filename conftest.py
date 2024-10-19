import requests
import pytest
from config import URL_REGISTER
from config import URL_LOGIN
from config import URL_LOGOUT
from config import URL_INGREDIENTS
import random

@pytest.fixture
def create_new_user():
    payload = {"email": f'new_user_{random.randint(1000, 9999)}@gmail.com',
                   "password": random.randint(10000, 99999), "name": f'Sasha{random.randint(1000, 9999)}'}
    response = requests.post(URL_REGISTER, data=payload)
    access_token = response.json()['accessToken']
    yield payload
    requests.delete(URL_REGISTER,headers={'Authorization': access_token})
@pytest.fixture
def login(create_new_user):
    payload = create_new_user
    response = requests.post(URL_LOGIN , data=payload)
    access_token = response.json()['accessToken']
    yield access_token
    refresh_token = response.json()['refreshToken']
    payload_1 = {"token": f"{refresh_token}"}
    requests.post(URL_LOGOUT, data=payload_1)
@pytest.fixture
def get_ingredients_id(create_new_user,login):
    response = requests.get(URL_INGREDIENTS, headers={'Authorization': login})
    return response.json()
