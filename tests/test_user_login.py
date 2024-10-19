import requests
from config import URL_LOGIN
import allure
from helpers import LoginData
from helpers import Answers
from config import URL_LOGOUT
class TestUserLogin:
    @allure.title('Проверка возможности логина под существующим пользователем')
    def test_login_existing_user_login_completed(self, create_new_user):
        response_1 = requests.post(URL_LOGIN, data=create_new_user)
        assert response_1.status_code == 200
        assert '"success":true' in response_1.text
        refresh_token =response_1.json()['refreshToken']
        payload_2 = {"token": f"{refresh_token}"}
        response_2 = requests.post(URL_LOGOUT, data=payload_2)
        assert response_2.status_code == 200
        assert response_2.text == Answers.logout_text
    @allure.title('Проверка невозможности логина с неверным логином и паролем')
    def test_user_login_with_incorrect_email_or_password_login_denied(self):
        payload = LoginData.incorrect_email_and_password
        response= requests.post(URL_LOGIN, data=payload)
        assert response.status_code == 401
        assert response.text == Answers.incorrect_data_text

