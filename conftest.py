import requests
from config import URL
from helpers import SignUpData
import pytest

@pytest.fixture
def create_new_user():
    payload = SignUpData.unique_user_data
    requests.post(f'{URL}/api/auth/register', data=payload)
    return payload