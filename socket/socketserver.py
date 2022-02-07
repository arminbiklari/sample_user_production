import sys , os 
import socket 
import json 
import datetime
import ast

def TCP_listener(host="127.0.0.1", port=1234):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
            s.bind((host, port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    time = datetime.datetime.now().strftime(("%H:%M:%S"))
                    print(f"{time} coonected by : {addr}")
                    data = conn.recv(1024)
                    return data
                    if not data:
                        continue
    except socket.error as msg:
        if socket.error == "Address already in use":
            print("Address already in use !!!")
if __name__ == "__main__":
    data = TCP_listener()
    data = data.decode("utf-8")
    data1 = json.loads(data)
    print(type(data1))
    print(data)
    # data = dict(data)
    # for key, value in json.loads(data).items():
    #     print(f"{key} : {value}")



# class TCP_server:
    
#     backlog = 5
#     client = None   # client socket

#     def __init__(self,host,port):
#         self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # create socket
#         self.socket.bind((host,port))                                   # bind socket
#         self.socket.listen(self.backlog)                                # listen socket

#     def accept(self):                                              # accept client
#         if self.client:                                       # if client is not None
#             self.client.close()                          # close client
#         self.client_socket, self.client_address = self.socket.accept()  # accept client
#         return self.client_socket, self.client_address  # return client socket and client address

#     def recieve(self):
#         data = self.socket.recv(1024)
#         return data
    
# server = TCP_server("127.0.0.1",1234)
# print(server.client)