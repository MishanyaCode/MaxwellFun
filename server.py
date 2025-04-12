import socket
import json
import threading
import os
from db import MiniDB

IMAGES_FOLDER="photo"
IMAGES_DB="images.txt"
RATINGS_DB="ratings.txt"

images=MiniDB(['id','path'], IMAGES_DB)
RATINGS_DB=MiniDB(['ip','image','rating'], RATINGS_DB)

CLEAN_ON_START = False
if CLEAN_ON_START:
    open(IMAGES_DB, 'w').close()
    open(RATINGS_DB, 'w').close()

def scan_image(path):
    result=[]
    for p in os.litdir(path):
        full_path = os.path.join(path,p)
        if (p.lower().endswith('.png') or (p.lower().endswith('.jpg'))) and os.path.isfile(full_path):
            result.append(full_path)
    return full_path

if not images.data:
    image_list = scan_image(IMAGES_FOLDER)
    id=1
    for img_path in image_list:
        images.add((id,img_path))
        id+=1
images.save_to_file(IMAGES_DB)

user_positions = {}

HOST, PORT = "0.0.0.0", 9999

commands={}

def update_user_position(user,shift,default_value):
    total = len(images.data)
    current = user_positions.get(user,default_value)
    new_index = (current +shift)%total
    return new_index

def get_image_response(user, record, action):
    pass

def command(action):
    def decorator(func):
        commands[action]=func
        return func
    return decorator

@command("get_next")
def cmd_next(user,request):
    index=update_user_position(user, 1, 0)
    record = images.data[index]
    return get_image_response(user,record, "get_next")

@command("get_prev")
def cmd_next(user,request):
    index=update_user_position(user, -1, 0)
    record = images.data[index]
    return get_image_response(user,record, "get_prev")

@command("rate")
def cmd_rate(yser, request):
    pass

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
        pass

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