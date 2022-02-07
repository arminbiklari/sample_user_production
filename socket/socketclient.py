import socket
import datetime
import os 
import json

json_path = "/home/armin/python_project/files/productions.json"

def create_dictionary(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)
        return data

def TCP_sender(host="127.0.0.1", port=1234, data=create_dictionary(json_path)):
    # data = {"productid": "1", "productname": "product1", "productprice": "100"}
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            data = json.dumps(data)
            s.sendall(bytes(data, "utf-8"))

    except socket.error as msg:
        print("Socket Error: ", msg)

TCP_sender()
