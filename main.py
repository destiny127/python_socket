import time
import threading
import socket

from zmq import DISCONNECT_MSG


FORMAT = "utf-8"
HEADER = 64
DISCONNECT_MSG = "!EXIT"
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

# --------------------------------------------------------------

def handle_client(conn,addr): 
    print(f"[CONNECTION ESTABLISHED] Server is connected to {addr} ...")
    connected = True

    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)

            if msg == DISCONNECT_MSG:
                connected = False

            print(f"[{addr}] Received : {msg}")
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {ADDR}....")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr)) 
        thread.start()

        print(f"[ACTIVE CONNECTION STARTED] {threading.active_count() -1 }")

print("[STARTING]  Server is running..." )
start()