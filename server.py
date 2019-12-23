import socket
import tqdm
import os
from _thread import *
import threading

print_lock = threading.Lock()
def threaded(c):
	recieved = client_socket.recv(buffer_size).decode()
	filename, filesize = recieved.split(seperator)
	filename = os.path.basename(filename)
	filesize = int(filesize)

	progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
	with open(filename, "wb") as f:
	    for _ in progress:
	        # read 1024 bytes from the socket (receive)
	        bytes_read = client_socket.recv(BUFFER_SIZE)
	        if not bytes_read:    
	            # nothing is received
	            # file transmitting is done
	            break
	        # write to the file the bytes we just received
	        f.write(bytes_read)
	        # update the progress bar
	        progress.update(len(bytes_read))

	# close the client socket
	client_socket.close()





def Main():

	server_host - '0.0.0.0'

	server_port = 10000
	buffer_size = 4096

	seperator = "<seperator>"

	s = socket.socket()

	s.bind((server_host, server_port))
	s.listen(5)

	print(f"[*] listening {server_host}:{server_port}")
	while True:
		client_socket, address = s.accept()
		print_lock.acquire()
		print(f"[+] {address} is connected")

		start_new_thread(threaded, (client_socket,))
	
	# close the server socket
	s.close()
