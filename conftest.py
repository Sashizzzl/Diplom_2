import requests
from config import URL
from helpers import SignUpData
import pytest

@pytest.fixture
def create_new_user():
    payload = SignUpData.unique_user_data
    response = requests.post(f'{URL}/api/auth/register', data=payload)
    return payload

@pytest.fixture
def login(create_new_user):
    payload = create_new_user
    response = requests.post(f'{URL}/api/auth/login', data=payload)
    access_token = response.json()['accessToken']
    yield access_token
    refresh_token = response.json()['refreshToken']
    payload_1 = {"token": f"{refresh_token}"}
    requests.post(f'{URL}/api/auth/logout', data=payload_1)
@pytest.fixture
def get_ingredients_id(create_new_user,login):
    response = requests.get(f'{URL}/api/ingredients', headers={'Authorization': login})
    return response.json()
