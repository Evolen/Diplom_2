import requests
import allure
from url import URL

class OrderMethods:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(body: dict):
        return requests.post(URL.ORDER, json = body, verify = False)