import mysql.connector
from mysql.connector import connect
from errno import errorcode


def create_user_db(database_name="Users", host="localhost", password="QWEr!@#4", user='root'):
    """
    this function for create User database
    """
    try:
        cnx = connect(user=user, password=password, host=host)
        cursor = cnx.cursor()    
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database_name))

        cnx.close()
        print("Database {} created successfully.".format(database_name))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print("already exists.")
        else:
            print(err.msg)
def create_user_table(database_name="Users", host="localhost", password="QWEr!@#4", user="root"):
    try:
        cnx = connect(user=user, password=password, host=host, database=database_name)
        cursor = cnx.cursor()
        cursor.execute("CREATE TABLE users (user_id INT NOT NULL AUTO_INCREMENT, user_name VARCHAR(255) NOT NULL, user_email VARCHAR(255) NOT NULL, user_password VARCHAR(255) NOT NULL, user_type VARCHAR(255) NOT NULL, user_created_at DATETIME NOT NULL, user_last_login DATETIME NOT NULL, is_enable BOOLEAN NOT NULL, PRIMARY KEY (user_id))")
        cnx.commit()
        cnx.close()
        print("Table users created successfully.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:    #Table already exists
            print("already exists.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:    #Database does not exist
            print("Database does not exist")
            create_user_db()
            create_user_table()
        else:
            print(err.msg)


def create_product_db(database_name="Products", host="localhost", password="QWEr!@#4"):
    """
    this function for create product database"""
    try :
        cnx = connect(user='root', password='QWEr!@#4', host='localhost')
        cursor = cnx.cursor()
        cursor.execute("CREATE DATABASE products")
        cnx.commit()
        cnx.close()
        print("Database products created successfully.")
    except mysql.connect.error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:  #Database already exists
            print("already exists.")
        else:
            print(err.msg)

def create_table_product(database_name="Products", host="localhost", password="QWEr!@#4", user="root"):
    """
    this function for create product table"""
    try:
        cnx = connect(user=user, password=password, host=host, database=database_name)
        cursor = cnx.cursor()
        cursor.execute("CREATE TABLE products (product_id INT NOT NULL AUTO_INCREMENT, product_name VARCHAR(255) NOT NULL, product_price INT NOT NULL, product_quantity INT NOT NULL, product_created_at DATETIME NOT NULL, product_updated_at DATETIME NOT NULL, PRIMARY KEY (product_id))")
        cnx.commit()
        cnx.close()
        print("Table products created successfully.")
    except mysql.connector.Error as err:    
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:     #Table already exists
            print("already exists.")     
        elif err.errno == errorcode.ER_BAD_DB_ERROR:     #Database does not exist
            print("Database does not exist")
            create_product_db()
            create_table_product()
        else:
            print(err.msg)