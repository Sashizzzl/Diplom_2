import requests
from config import URL
from helpers import SignUpData
import allure
import pytest
class TestUserSignUp:
    @allure.title('Проверка возможности создания уникального пользователя')
    def test_create_user_with_unique_data_user_created(self):
        payload = SignUpData.unique_user_data
        response = requests.post(f'{URL}/api/auth/register', data=payload)
        assert response.status_code == 200
        assert '"success":true' in response.text
    @allure.title('Проверка невозможности создания пользователя, который уже зарегистрирован')
    def test_create_user_which_already_created_user_not_created_for_the_second_time(self):
        payload = SignUpData.double_sign_in
        response_1 = requests.post(f'{URL}/api/auth/register', data=payload)
        assert response_1.status_code == 200
        response_2 = requests.post(f'{URL}/api/auth/register', data=payload)
        assert response_2.status_code == 403
        assert response_2.text == '{"success":false,"message":"User already exists"}'
    @allure.title('Проверка невозможности создания пользователя при незаполнении одно из обязательных полей')
    @pytest.mark.parametrize('payload_data',[SignUpData.user_data_no_email,SignUpData.user_data_no_password,SignUpData.user_data_no_name])
    def test_create_user_without_one_of_required_data_user_not_created(self,payload_data):
        payload = payload_data
        response = requests.post(f'{URL}/api/auth/register', data=payload)
        assert response.status_code == 403
        assert response.text == '{"success":false,"message":"Email, password and name are required fields"}'

