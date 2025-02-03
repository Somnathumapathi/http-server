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
        req_content = client_request.split('\n')
        req_first_line = req_content[0]
        req_method = req_first_line.split(' ')[0]
        req_path = req_first_line.split(' ')[1]
        # print(req_path)
        response = ""
    
        if req_method == "GET":

            try:

                if req_path == "/":
                    with open("index.html") as f:
                        content = f.read()
                    response = "HTTP/1.1 200 OK\n\n" + content

                elif req_path == "/test":
                    with open("test.json") as f:
                        content = f.read()
                    response = "HTTP/1.1 200 OK\n\n" + content

                else:
                    response = "HTTP/1.1 404 Not Found\n\nPage Not Found"


            except FileNotFoundError:
                response = "HTTP/1.1 404 Not Found\n\nFile Not Found"

                
        else:
            response = "HTTP/1.1 405 Method Not Allowed\n\nAllow: GET"
               
        client_socket.sendall(response.encode())
        client_socket.close()
    # try:
    #     client_socket, client_address = server_socket.accept()
    #     print(client_socket)
    #     print(client_address)
    # except:
    #     time.sleep(1)
    #     continue

