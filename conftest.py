import pytest

from generators import generate_random_user_dict
from api_methods.user_methods import UserMethods

@pytest.fixture(scope="function")
def create_user():
    user_body = generate_random_user_dict()
    response = UserMethods.create_user(body = user_body)
    yield user_body
    user_login= {
        "email": user_body["email"],
        "password": user_body["password"]
    }
    response = UserMethods.login_user(body = user_login)
    access_token = response.json()["accessToken"]
    headers = {
        "Authorization": access_token
    }
    response = UserMethods.delete_user(headers)
    

@pytest.fixture(scope="function")
def login_user():
    user_body = generate_random_user_dict()
    response = UserMethods.create_user(body = user_body)
    user_login= {
        "email": user_body["email"],
        "password": user_body["password"]
    }
    response = UserMethods.login_user(body = user_login)
    access_token = response.json()["accessToken"]
    headers = {
        "Authorization": access_token
    }
    yield headers
    response = UserMethods.delete_user(headers)