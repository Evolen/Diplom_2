import pytest
import allure

from api_methods.create_user_methods import CreateUserMethods


class TestCreateUser:

    @allure.title("Создание пользователя")
    @allure.description("Проверка создания уникального пользователя")
    def test_create_user(self, create_random_user):    
        response = CreateUserMethods.create_user(user_data = create_random_user)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.json()["success"] == True          
        

    @allure.description("Проверка создания пользователя, который уже был создан")
    def test_create_user_again(self, create_random_user):        
        response = CreateUserMethods.create_user(user_data=create_random_user)
        response = CreateUserMethods.create_user(user_data=create_random_user)
        assert response.status_code == 403, f"Expected status code 403, but got {response.status_code}"
        assert response.json()["success"] == False
        assert response.json()["message"] == "User already exists"

    @allure.description("Проверка создания пользователя без указания пароля")
    def test_create_user_without_pass (self, create_user_without_pass):
        response = CreateUserMethods.create_user(user_data = create_user_without_pass)   
        assert response.status_code == 403, f"Expected status code 403, but got {response.status_code}"
        assert response.json()["success"] == False
        assert response.json()["message"] == "Email, password and name are required fields"

  
