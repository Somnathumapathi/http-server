import socket
# import time

SERVER_CONFIG = ("0.0.0.0", 8080)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.setblocking(False)

server_socket.bind(SERVER_CONFIG)

server_socket.listen(7)

print(f"Listening to port {SERVER_CONFIG[1]}")
while True:
        client_socket, client_address = server_socket.accept()
        client_request = client_socket.recv(1024).decode()
        print(f"Received request from {client_address}: {client_request}")
        # print(client_socket)
        # print(client_address)
    # try:
    #     client_socket, client_address = server_socket.accept()
    #     print(client_socket)
    #     print(client_address)
    # except:
    #     time.sleep(1)
    #     continue

