Ransomware
	server-
		server.py - listens for the target to run ransomware.py and recieves key 
		sendkey.py - sends the key onces payment is verified
	target-
		ransomware.py - encrypts files, sends key and deletes after
		listen.py - listens for decrypt message from server and recieves key, then decrypts 

convert to .exe and run on victim machine

serverside client for ransomware


This is for purely for educational purposes, not to be used in any malicious or illegal manner.
The intent of this repository is to educate about how ransomware works and how it is created.