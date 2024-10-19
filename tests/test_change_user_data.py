import requests
from config import URL
import allure
from helpers import ChangeUserData
import pytest
class TestChangeUserData:
    @allure.title('Проверка возможности изменения данных авторизованного пользователя')
    @pytest.mark.parametrize('payload,expected_text', [[ChangeUserData.name, ChangeUserData.name["name"]],
                                                       [ChangeUserData.email, ChangeUserData.email["email"]]])
    def test_change_authorized_user_data_change_completed(self,create_new_user,login,payload,expected_text):
        response = requests.patch(f'{URL}/api/auth/user', headers={'Authorization': login},data=payload)
        assert response.status_code == 200
        assert expected_text in response.text
    @allure.title('Проверка невозможности изменения данных неавторизованного пользователя')
    @pytest.mark.parametrize('payload', [ChangeUserData.name, ChangeUserData.email])
    def test_change_unauthorized_user_data_change_incompleted(self,create_new_user,payload):
        response = requests.patch(f'{URL}/api/auth/user', data=payload)
        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"You should be authorised"}'

#response_1 = requests.get(f'{URL}/api/auth/user', headers={'Authorization': login})
        #assert response_1.status_code == 200
        #assert response_1.text == f'{{"success":true,"user":{{"email":"{create_new_user["email"]}","name":"{create_new_user["name"]}"}}}}'