import socket
import os
import sys


def Main():



	host = '0.0.0.0'
	port = 10000
	
	s = socket.socket()
	s.bind((host, port))
	print("started listening")
	s.listen(1)
	while True:
		c, addr = s.accept()
		print("connection from: " + addr[0])
		filename = addr[0].replace('.', '-') + '.key'
		file = open(filename, "wb")
		while True:
			data = c.recv(1024)
			if not data:
				break
			file.write(data)
		print("from connected user: " + filename)
		file.close()
		c.close()

if __name__ == '__main__':
	Main()