import pytest
import allure


from api_methods.order_methods import OrderMethods
from api_methods.user_methods import UserMethods
from generators import *
from data import *

class TestCreateOrder:

    @allure.title("Создание заказа")
    @allure.description("Проверка создания заказа с авторизацией и ингридиентов")    
    def test_create_order_with_login(self, login_user):
        with allure.step("Отправляем запрос на создание заказа"):
            response = OrderMethods.create_order(body=CREATE_ORDER_INGREDIENTS)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.json()["success"] == True 
        assert response.json()["name"] == "Флюоресцентный бессмертный бургер" 
        
    @allure.description("Проверка создания заказа без авторизации")    
    def test_create_order_without_login(self):       
        with allure.step("Отправляем запрос на создание заказа"):
            response = OrderMethods.create_order(body=CREATE_ORDER_INGREDIENTS)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.json()["success"] == True 
        assert response.json()["name"] == "Флюоресцентный бессмертный бургер" 
   
    @allure.description("Проверка создания заказа без ингридиентов")    
    def test_create_order_without_ingredients(self) :       
        with allure.step("Отправляем запрос на создание заказа"):
            response = OrderMethods.create_order(body=CREATE_ORDER_WITHOUT_INGREDIENTS)
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

        
    @allure.description("Проверка создания заказа с неверным хешем ингредиента")    
    def test_create_order_fake_hash_ingredients(self) :       
        with allure.step("Отправляем запрос на создание заказа"):
            response = OrderMethods.create_order(body=FAKE_HASH_INGREDIENTS)
        assert response.status_code == 500, f"Expected status code 500, but got {response.status_code}"






























    
       

