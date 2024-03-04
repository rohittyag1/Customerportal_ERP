import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen()

print("Server listening on 0.0.0.0:12345")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Received data: {data.decode()}")

client_socket.close()

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('server_ip', 12345)

client_socket.connect(server_address)

while True:
    message = input("Enter message to send: ")
    client_socket.send(message.encode())

client_socket.close()


