import requests
import allure
from url import URL

class OrderMethods:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(order_data: dict):
        return requests.post(URL.ORDER, json=order_data, verify = False)

    @staticmethod
    @allure.step("Создание заказа без ингридиентов")
    def create_order_without_ingridients(order_data: dict):
        return requests.post(URL.ORDER, json=order_data, verify = False)    

    @staticmethod
    @allure.step("Создание заказа с неверным хешем ингридиентов")
    def create_order_fake_ingredients(order_data: dict):
        return requests.post(URL.ORDER, json=order_data, verify = False)      