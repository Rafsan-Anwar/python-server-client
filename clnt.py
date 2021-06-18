import socket

SERVER = '192.168.0.106'
PORT = 5000
ADDR = (SERVER, PORT)

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = 'DISCONNECT!'

print(socket.gethostbyname(socket.gethostname()))

# create a socket(client) with IP and and PORT
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
	messsage = msg.encode(FORMAT)
	msg_length = len(messsage)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(messsage)
	print(client.recv(2048).decode(FORMAT))




text=str(input())
send(text)
send(DISCONNECT_MSG)

# py servr.py
# py clnt.py


