import pytest

from generators import generate_random_user_dict
from api_methods.create_user_methods import CreateUserMethods
from api_methods.login_user_methods import LoginUserMethods
from api_methods.create_order_methods import OrderMethods
from data import *


    
@pytest.fixture
def create_random_user(scope="function"):
    user_body = generate_random_user_dict()    
    return user_body

@pytest.fixture
def create_user_without_pass(scope="function"):
    user_body = CREATE_USER_WITHOUT_PASS   
    return user_body 

@pytest.fixture
def create_user(scope="function"):
    user_body = generate_random_user_dict()
    response = CreateUserMethods.create_user(user_data = user_body) 
    return user_body

@pytest.fixture
def login_user(scope="function"):
    user_body = generate_random_user_dict()
    response = CreateUserMethods.create_user(user_data = user_body)
    user_login={"email": user_body["email"], "password":user_body["password"]}
    response = LoginUserMethods.login_user(user_data = user_login)   
    return user_body

@pytest.fixture
def fake_pass_email_login(scope="function"):
    user_body = FAKE_LOGIN_AND_PASS
    return user_body    

@pytest.fixture
def create_order(scope="function"):
    order_body = CREATE_ORDER_INGREDIENTS
    return order_body 

@pytest.fixture
def create_order_no_ingredients(scope="function"):
    order_body = CREATE_ORDER_WITHOUT_INGREDIENTS 
    return order_body     
 
@pytest.fixture
def create_order_fake_hash(scope="function"):
    order_body = FAKE_HASH_INGREDIENTS    
    return order_body 
