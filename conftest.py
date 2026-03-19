import pytest

from generators import generate_random_user_dict
from api_methods.user_methods import UserMethods

@pytest.fixture(scope="function")
def create_user():
    create_user_body = generate_random_user_dict()
    create_user_response = UserMethods.create_user(body = create_user_body)
    yield create_user_body
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
    

@pytest.fixture(scope="function")
def login_user():
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
    yield headers
    delete_user_response = UserMethods.delete_user(headers = headers)