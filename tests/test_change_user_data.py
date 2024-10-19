import requests
from config import URL_AUTH
import allure
from helpers import ChangeUserData
import pytest
from helpers import Answers
class TestUserDataChange:
    @allure.title('Проверка возможности изменения данных авторизованного пользователя')
    @pytest.mark.parametrize('payload,expected_text', [[ChangeUserData.name, ChangeUserData.name["name"]],
                                                      [ChangeUserData.email, ChangeUserData.email["email"]],[ChangeUserData.password, Answers.success_text]])
    def test_change_authorized_user_data_change_completed(self,create_new_user,login,payload,expected_text):
        response = requests.patch(URL_AUTH, headers={'Authorization': login},data=payload)
        assert response.status_code == 200
        assert expected_text in response.text
    @allure.title('Проверка невозможности изменения данных неавторизованного пользователя')
    @pytest.mark.parametrize('payload', [ChangeUserData.name, ChangeUserData.email])
    def test_change_unauthorized_user_data_change_incompleted(self,create_new_user,payload):
        response = requests.patch(URL_AUTH, data=payload)
        assert response.status_code == 401
        assert response.text == Answers.need_authorization_text

