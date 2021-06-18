import socket
import threading

# get ip address of localhost and set port to run on
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = '192.168.0.106'
PORT = 5000
ADDR = (SERVER, PORT)

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = 'DISCONNECT!'

# create a socket(server) with IP and and PORT
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# handling each connection
def handle_client(conn, addr):
	# the client who is connected
	print("[NEW CONNECTION] ", addr," connected.")
	# handling connection
	connected = True
	while connected:
		# identifying msg length
		msg_length = conn.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			# receive the actual message
			msg = conn.recv(msg_length).decode(FORMAT)
			if msg == DISCONNECT_MSG:
				connected = False
			print(addr," : ",msg)
			# Server replies with a response
			conn.send("Msg received".encode(FORMAT))

	conn.close()



# initiating server function
def start():
	# server begins listening
	server.listen()
	print("[listening] server is listening on ", SERVER, ":", PORT)

	while True:
		conn, addr = server.accept()
		# server selects a thread to handle new request
		thread = threading.Thread(target = handle_client, args = (conn, addr))
		thread.start()
		# prints total active connections
		print("[ACTIVE CONNECTIONS] ", threading.activeCount()-1)


print('[STARTING] server is starting...')
start()








