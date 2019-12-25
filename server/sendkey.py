import socket
import os
import sys



def send_file(file_name, host, port):
        s = socket.socket()
        s.connect((host, port))
        print("trying to connect")

        file = open(file_name, "rb")
        l = file.read(1024)
        while(l):
                s.send(l)
                l = file.read(1024)
        s.shutdown(socket.SHUT_WR)
        file.close()
        s.close()
        

def main():
        send_file("10-0-0-14.key", "10.0.0.28", 10000 )

if __name__ == '__main__':
        main()