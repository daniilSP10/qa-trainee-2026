import random
from faker import Faker

fake = Faker()

def generate_seller_id():
    return random.randint(111111, 999999)

def generate_item_name():
    return fake.catch_phrase()

def generate_price():
    return random.randint(1, 100000)