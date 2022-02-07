# import string
# import random
# import datetime
# from unicodedata import name
from errno import errorcode
from mysql.connector import connect
import mysql.connector
# class User:
#     """
#     this for create user and create details of user  
#     and return user_id, user_password, user_last_login, user_created_at
#     """
#     def __init__(self, user_name, user_email, user_type):
#         self.user_name = user_name
#         self.user_email = user_email
#         self.user_type = user_type
#         self.user_created_at = datetime.datetime.now().replace(microsecond=0) # when user created this run for one time 
#         # self.generate_user_password = self.generate_user_password()
#         self.user_id = self.generate_user_id()
#         # self.__user_last_login = self.user_last_login()
#         self.is_enable = True
        
#     def generate_user_id(self):
#         """
#         this method for generate user_id"""
#         self.user_id = random.randint(1, 100)
#         return self.user_id

#     user_name = ""
#     user_email = ""
#     user_password = ""
#     user_id = ""
#     user_type = ""
#     user_created_at = ""
#     user_last_login = ""

# Email = "armin76a@gmail.com"
# name = "armin"
# type = "admin"

# person = User(name, Email, type)
# print(f"your username is {person.user_name} and your email is {person.user_email} and you are {person.user_type} and your user_id is {person.user_id}")

try :
    cnx = connect(user='root', password='QWEr!@#4', host='localhost')
    cursor = cnx.cursor()
    cursor.execute("CREATE DATABASE test1")
    cnx.commit()
    cnx.close()
    print("Database products created successfully.")
except mysql.connect.error as err:
    if err.errno == errorcode.ER_DB_CREATE_EXISTS:  #Database already exists
        print("already exists.")
    else:
        print(err.msg)
