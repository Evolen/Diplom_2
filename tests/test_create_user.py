import pytest
import allure

from api_methods.user_methods import UserMethods
from generators import *
from data import *

class TestCreateUser:

    @allure.title("Создание пользователя")
    @allure.description("Проверка создания уникального пользователя")
    def test_create_user(self):
        create_user_body = generate_random_user_dict()
        create_user_response = UserMethods.create_user(body = create_user_body)
        login_user_body = {
            "email": create_user_body["email"],
            "password": create_user_body["password"]
        }
        login_user_response = UserMethods.login_user(body = login_user_body)
        access_token = login_user_response.json()["accessToken"]
        headers = {
            "Authorization": access_token
        }
        delete_user_response = UserMethods.delete_user(headers = headers)
        assert create_user_response.status_code == 200, f"Expected status code 200, but got {create_user_response.status_code}"
        assert create_user_response.json()["success"] == True          
        

    @allure.description("Проверка создания пользователя, который уже был создан")
    def test_create_user_again(self):
        create_user_body = generate_random_user_dict()
        create_user_response = UserMethods.create_user(body = create_user_body)
        create_user_response = UserMethods.create_user(body = create_user_body)
        login_user_body = {
            "email": create_user_body["email"],
            "password": create_user_body["password"]
        }
        login_user_response = UserMethods.login_user(body = login_user_body)
        access_token = login_user_response.json()["accessToken"]
        headers = {
            "Authorization": access_token
        }
        delete_user_response = UserMethods.delete_user(headers = headers)
        assert create_user_response.status_code == 403, f"Expected status code 403, but got {create_user_response.status_code}"
        assert create_user_response.json()["success"] == False
        assert create_user_response.json()["message"] == "User already exists"

    @allure.description("Проверка создания пользователя без указания пароля")
    def test_create_user_without_pass (self):
        create_user_body = CREATE_USER_WITHOUT_PASS
        create_user_response = UserMethods.create_user(body = create_user_body)   
        assert create_user_response.status_code == 403, f"Expected status code 403, but got {create_user_response.status_code}"
        assert create_user_response.json()["success"] == False
        assert create_user_response.json()["message"] == "Email, password and name are required fields"

  
