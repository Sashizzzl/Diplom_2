import requests
from config import URL
import allure
from helpers import Ingredients
class TestCreateOrder:
    @allure.title('Проверка возможности создания заказа с авторизацией')
    def test_create_order_with_authorization_order_created(self,login,get_ingredients_id):
        payload = {'ingredients': get_ingredients_id['data'][0]['_id']}
        response = requests.post(f'{URL}/api/orders', headers = {'Authorization': login}, data = payload)
        assert response.status_code == 200
        assert get_ingredients_id['data'][0]['_id'] and '"success":true' in response.text
    @allure.title('Проверка возможности создания заказа без авторизации')
    def test_create_order_unauthorized_user_order_created(self):
        payload = {'ingredients': Ingredients.correct_id}
        response = requests.post(f'{URL}/api/orders', data = payload)
        assert response.status_code == 200
        assert '"success":true' in response.text
    @allure.title('Проверка возможности создания заказа с ингредиентами')
    def test_create_order_with_igredients_order_created(self,login,get_ingredients_id):
        payload = {'ingredients': [get_ingredients_id['data'][0]['_id'],get_ingredients_id['data'][1]['_id']]}
        response = requests.post(f'{URL}/api/orders', headers={'Authorization': login}, data=payload)
        assert response.status_code == 200
        assert get_ingredients_id['data'][0]['_id'] and get_ingredients_id['data'][1]['_id'] and'"success":true' in response.text
    @allure.title('Проверка невозможности создания заказа без ингредиентов')
    def test_create_order_with_no_igredients_order_impossible_to_create(self,login,get_ingredients_id):
        payload = {'ingredients': ''}
        response = requests.post(f'{URL}/api/orders', headers={'Authorization': login}, data=payload)
        assert response.status_code == 400
        assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'
    @allure.title('Проверка невозможности создания заказа с неверным хешем ингредиентов')
    def test_create_order_with_incorrect_ingredient_id_order_impossible_to_create(self,login):
        payload = {'ingredients': Ingredients.incorrect_id}
        response = requests.post(f'{URL}/api/orders', headers={'Authorization':login}, data = payload)
        assert response.status_code == 500
        assert 'Server Error' in response.text

