import requests
import allure
from url import URL

class UserMethods:

    @staticmethod
    @allure.step("Создание пользователя")
    def create_user(body: dict):
        return requests.post(URL.CREATE_USER, json = body, verify = False)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(headers: dict):
        return requests.delete(URL.DELETE_USER, headers = headers, verify = False)

    @staticmethod
    @allure.step("Логин пользователя")
    def login_user(body: dict):
        return requests.post(URL.LOGIN_USER, json = body, verify = False)