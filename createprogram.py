from errno import errorcode
from user_production import *
from mysql.connector import connect
import mysql.connector
from helps  import *
from database import *
import os, sys


while True:
    """
    this for create user aor product and import if user want to database"""
    print_main()  # this for print help for create user
    choise = input("please enter your choise: ")
    if choise == "1":
        Help_create_user()
        try:
            username = str(input("Enter your username: "))
            Email = str(input("Enter your Email: "))
            type = str(input("Enter your type  of user (admin / supervisor / guest): "))
        except:
            print("Please enter a valid string ")
            continue
        if username == "" or Email == "" or type == "":
            print("Please enter a valid input !!")
            continue
        person = User(username, Email, type)
        print(f"your username is {person.user_name} and your email is {person.user_email} and you are {person.user_type}")
        print(f"your password is {person.user_password} \t keep it safe !")
        try:    
            connector = connect(host='localhost', database='Users', user='root', password='QWEr!@#4')
            cursor = connector.cursor()
            cursor.execute("""INSERT INTO users (user_name, user_email, user_type, user_password, user_created_at, user_last_login, is_enable) VALUES (%s, %s, %s, %s, %s, %s, %s)""", (person.user_name, person.user_email, person.user_type, person.user_password, person.user_created_at, person.user_last_login, person.is_enable))
            connector.commit()
            connector.close()
            print("user created successfully")
            print(f"this account created at {person.user_created_at}")
        except mysql.connector.Error as err:
            if err.msg.find("Duplicate entry") != -1:
                print("user already exists")
            elif err.msg.find("Incorrect string value") != -1:
                print("Please enter a valid string")
            elif err.msg.find("Database does not exist") != -1:
                print("Database does not exist")
                create_user_db()
                create_user_table()
                continue
            elif err.msg.find("Table does not exist") != -1:
                create_user_table()
                continue
            elif err.msg.find("Unknown database") != -1:
                print("Database does not exist")
                create_user_db()
                create_user_table()
                continue
            else:
                print(err.msg)
                continue
        if str(input("do you want to continue? (y/n): ")).lower() == "y":
            print("press Enter to continue")
            input()
            continue
        else:
            if str(input("do you want to continue? (y/n): ")).lower() == "n":
                print("press Enter to exit")
                input()
                break
            else:
                print("please enter a valid input")
                continue
    elif choise == "2":
        Help_create_product()
        try: 
            product_name = str(input("Enter your product_name: "))
            product_price = int(input("Enter your product_price: "))
            product_quantity = int(input("Enter your product_quantity: "))
        except:
            print("Please enter a valid input ")
            continue
        if product_name == "" or product_price == "" or product_quantity == "":
            print("Please enter a valid input !!")
            continue
        product = product(product_name, product_price, product_quantity)
        print(f"your product_name is {product.product_name} and your product_price is {product.product_price} and your product_quantity is {product.product_quantity}")
        print(f"product created at {product.product_created_at}")
        try:
            connectore = connect(host='localhost', database='products', user='root', password='QWEr!@#4')      
            cursor = connector.cursor()
            cursor.execute("""INSERT INTO products (product_name, product_price, product_quantity, product_created_at) VALUES (%s, %s, %s, %s)""", (product.product_name, product.product_price, product.product_quantity, product.product_created_at))  
            connector.commit()
            connector.close()
            print("product created successfully")
        except:
            if err.msg.find("Duplicate entry") != -1:
                print("product already exists")
            elif err.msg.find("Incorrect string value") != -1:
                print("Please enter a valid string")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:  
                print("Database does not exist")
                create_product_db()
                create_table_product()
                continue
            else:
                print(err.msg)
                continue
        if str(input("do you want to continue? (y/n): ")).lower() == "y":
            print("press Enter to continue")
            input()
            continue
        elif str(input("do you want to continue? (y/n): ")).lower() == "n":
            print("press Enter to exit")
            input()
            break
    elif choise == "3":
        Help_search()
        try:
            search = str(input("Enter name or email for search: "))
        except ValueError:
            print("Please enter a valid string ")
            continue
        if search == "":
            print("Please enter a valid input !!")
            continue
        try:
            connector = connect(host='localhost', database='users', user='root', password='QWEr!@#4')
            cursor = connector.cursor()
            cursor.execute("""SELECT * FROM users WHERE user_name = %s OR user_email = %s""", (search, search))
            result = cursor.fetchall()
            if result == []:
                print("user not found")
            elif result:
                print(result)
            connector.close()
            if result:
                print(result)
            else:
                print("no result")
        except mysql.connector.Error as err:
            if err.errno == errorcode.DatabaseError:
                print("Database does not exist")
                create_user_db()
                continue
            else:
                print(err.msg)
                continue
        if str(input("do you want to continue? (y/n): ")).lower() == "y":
            print("press Enter to continue")
            input()
            continue
        elif str(input("do you want to continue? (y/n): ")).lower() == "n":
            print("press Enter to exit")
            input()
            break
        else:
            print("bad input !!")
            break
    elif choise == "4":
        product_search()
        try:
            product_search = str(input("Enter just name for search: "))
        except ValueError:
            print("please Enter a valid input ")
            continue
        if product_search == "":
            print("Please enter a valid input !!")
            continue
        try:
            connector = connect(host='localhost', database='products', user='root', password='QWEr!@#4')
            cursor = connector.cursor()
            cursor.execute("""SELECT * FROM products WHERE product_name = %s""", (product_search,))
            result = cursor.fetchall()
            connector.commit()
            connector.close()
            if result:
                print(result)
            elif result == []:
                print("product not found")
        except mysql.connector.Error as err:     #if database does not exist
            print(err.msg)
            continue
        if str(input("do you want to continue? (y/n): ")).lower() == "y":
            print("press Enter to continue")
            input()
            continue
        elif str(input("do you want to continue? (y/n): ")).lower() == "n":
            print("press Enter to exit")
            input()
            break
        else:
            print("bad input !!")
            break
    elif choise == "5":
        print("good bye")
        break
    else:
        print("bad input !!")
        continue

