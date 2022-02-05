from random import randint
import datetime      
import random
import string

class User:
    """
    this for create user and create details of user  
    and return user_id, user_password, user_last_login, user_created_at
    """
    def __init__(self, user_name, user_email, user_type):
        self.user_name = user_name
        self.user_email = user_email
        self.user_type = user_type
        self.user_created_at = datetime.datetime.now().replace(microsecond=0) # when user created this run for one time 
        self.user_password = self.generate_user_password()
        self.user_id = self.generate_user_id()
        self.__user_last_login = self.user_last_login()
        self.is_enable = True

    user_name = ""
    user_email = ""
    user_password = ""
    user_id = ""
    user_type = ""
    user_created_at = ""
    user_last_login = ""
    is_enable = True
    def generate_user_id(self):
        """
        this method for generate user_id"""
        self.user_id = randint(1, 100)
        return self.user_id
    def generate_user_password(self):
        """
        this method for generate user_password"""
        self.user_password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        return self.user_password
    def user_last_login(self):
        """
        this method for generate user_last_login"""
        self.__user_last_login = datetime.datetime.now()
        return self.user_last_login
 
class Product:
    """
    this class for products and create a products with attributes"""
    def __init__(self, product_id, product_name, product_price, product_quantity):
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.product_created_at = datetime.datetime.now() 
    product_name = ""
    product_id = ""
    product_price = ""
    product_quantity = ""
    product_created_at = ""
    product_updated_at = ""

    def product_id(self):
        """
        this method for generate product_id"""
        self.product_id = randint(360, 1000)
        return self.product_id

    def update_product_price(self, product_price):
        """
        this method for update product_price"""
        self.product_price = product_price
        self.product_updated_at = datetime.datetime.now()
        return self.product_price, self.product_updated_at

    def update_product_quantity(self, product_quantity):
        """
        this method for update product_quantity"""
        self.product_quantity = product_quantity
        self.product_updated_at = datetime.datetime.now()
        return self.product_quantity, self.product_updated_at
