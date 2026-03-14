import requests
import allure
from url import URL


class LoginUserMethods:

    @staticmethod
    @allure.step("Логин пользователя")
    def login_user(user_data: dict):
        return requests.post(URL.LOGIN_USER, json = user_data, verify = False)

    @staticmethod
    @allure.step("Проверка входа с неверным логином и паролем")
    def fake_login_user(user_data: dict):
        return requests.post(URL.LOGIN_USER, json = user_data, verify = False)

  
     

        