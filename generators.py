from faker import Faker
fake = Faker()



def generate_random_user_dict():
    return {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
     
    }
    
    