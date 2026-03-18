import pytest
import allure

from api_methods.user_methods import UserMethods
from generators import *
from data import *

class TestCreateUser:

    @allure.title("Создание пользователя")
    @allure.description("Проверка создания уникального пользователя")
    def test_create_user(self):
        create_random_user = generate_random_user_dict()
        response = UserMethods.create_user(body = create_random_user)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.json()["success"] == True          
        

    @allure.description("Проверка создания пользователя, который уже был создан")
    def test_create_user_again(self):
        create_random_user = generate_random_user_dict()
        response = UserMethods.create_user(body=create_random_user)
        response = UserMethods.create_user(body=create_random_user)
        assert response.status_code == 403, f"Expected status code 403, but got {response.status_code}"
        assert response.json()["success"] == False
        assert response.json()["message"] == "User already exists"

    @allure.description("Проверка создания пользователя без указания пароля")
    def test_create_user_without_pass (self):
        response = UserMethods.create_user(body = CREATE_USER_WITHOUT_PASS)   
        assert response.status_code == 403, f"Expected status code 403, but got {response.status_code}"
        assert response.json()["success"] == False
        assert response.json()["message"] == "Email, password and name are required fields"

  
