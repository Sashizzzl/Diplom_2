import requests
from config import URL_ORDERS
import allure
from helpers import Ingredients
from helpers import Answers
class TestCreateOrder:
    @allure.title('Проверка возможности создания заказа с авторизацией')
    def test_create_order_with_authorization_order_created(self,create_new_user,login,get_ingredients_id):
        payload = {'ingredients': get_ingredients_id['data'][0]['_id']}
        response = requests.post(URL_ORDERS, headers = {'Authorization': login}, data = payload)
        assert response.status_code == 200
        assert get_ingredients_id['data'][0]['_id'] and Answers.success_text in response.text
    @allure.title('Проверка возможности создания заказа без авторизации')
    def test_create_order_unauthorized_user_order_created(self):
        payload = {'ingredients': Ingredients.correct_id}
        response = requests.post(URL_ORDERS, data = payload)
        assert response.status_code == 200
        assert Answers.success_text in response.text
    @allure.title('Проверка возможности создания заказа с ингредиентами')
    def test_create_order_with_igredients_order_created(self,create_new_user,login,get_ingredients_id):
        payload = {'ingredients': [get_ingredients_id['data'][0]['_id'],get_ingredients_id['data'][1]['_id']]}
        response = requests.post(URL_ORDERS, headers={'Authorization': login}, data=payload)
        assert response.status_code == 200
        assert get_ingredients_id['data'][0]['_id'] and get_ingredients_id['data'][1]['_id'] and Answers.success_text in response.text
    @allure.title('Проверка невозможности создания заказа без ингредиентов')
    def test_create_order_with_no_igredients_order_impossible_to_create(self,create_new_user,login,get_ingredients_id):
        payload = {'ingredients': ''}
        response = requests.post(URL_ORDERS, headers={'Authorization': login}, data=payload)
        assert response.status_code == 400
        assert response.text == Answers.need_ids_text
    @allure.title('Проверка невозможности создания заказа с неверным хешем ингредиентов')
    def test_create_order_with_incorrect_ingredient_id_order_impossible_to_create(self,login):
        payload = {'ingredients': Ingredients.incorrect_id}
        response = requests.post(URL_ORDERS, headers={'Authorization':login}, data = payload)
        assert response.status_code == 500
        assert Answers.server_error_text in response.text

