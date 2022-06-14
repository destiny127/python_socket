import socket

FORMAT = "utf-8"
HEADER = 64
DISCONNECT_MSG = "!EXIT"
PORT = 5050
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)