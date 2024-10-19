import requests
from config import URL_ORDERS
import allure
from helpers import Answers
class TestGetUseOrders:
    @allure.title('Проверка возможности получения списка заказов конкретного пользователя с авторизацией')
    def test_get_user_orders_with_authorization_list_of_orders_returned(self,login):
        response = requests.get(URL_ORDERS, headers={'Authorization': login})
        assert response.status_code == 200
        assert Answers.success_text in response.text
    @allure.title('Проверка невозможности получения списка заказов конкретного пользователя без авторизации')
    def test_get_user_orders_no_authorization_list_of_orders_no_return_need_authorization(self):
        response = requests.get(URL_ORDERS)
        assert response.status_code == 401
        assert response.text == Answers.need_authorization_text
