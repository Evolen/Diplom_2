import requests
import allure
from url import URL


class CreateUserMethods:

    @staticmethod
    @allure.step("Создание пользователя")
    def create_user(user_data: dict):
        return requests.post(URL.CREATE_USER, json = user_data, verify = False)


 
        
