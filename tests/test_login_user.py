import pytest
import allure

from api_methods.login_user_methods import LoginUserMethods

class TestLoginCourier:

    @allure.title("Проверка логина")
    @allure.description("Проверка существующего логина")
    def test_login_user(self, create_user):
        user_login={"email": create_user["email"], "password":create_user["password"]}
        response = LoginUserMethods.login_user(user_data = user_login)   
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.json()["success"] ==True
        assert response.json()["user"]["email"] == create_user["email"]
        assert response.json()["user"]["name"] == create_user["name"]

    
    @allure.description("Проверка на ошибку, если неправильно указать логин и пароль")
    def test_fake_login_user(self, fake_pass_email_login):
        response = LoginUserMethods.fake_login_user(user_data = fake_pass_email_login)  
        assert response.status_code == 401, f"Expected status code 401 but got {response.status_code}"
        assert response.json()["success"] == False
        assert response.json()["message"] == "email or password are incorrect"

   