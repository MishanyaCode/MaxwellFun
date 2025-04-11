import socket
import json
import threading
import os

IMAGES_FOLDER="photo"
IMAGES_DB="images.txt"
RATINGS_DB="ratings.txt"
HOST, PORT = "0.0.0.0", 9999

def handle_client(client_socket, address):
    user_id=address[0]
    try:
        while True:
            data=client_socket.recv(1024).decode()
            if not data:
                break
            request = json.loads(data)
            action = request.get("action")
            #handler commands: rate, get_next
            response=None
            client_socket.send(json.dumps(response).encode())
    except:

def start_server():
    server = server.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)
    print(f"server is listening on port {PORT}")
    while True:
        client_socket, addr = server.accept()
        print(f"Connected client: {addr}")
        #thread
if __name__=='__main__':
    start_server()