#!/usr/bin/env python
import sys
import socket
from messageformat import *

def startclient(params):
	if len(params) < 2:
		print "Need a server name/IP to connect"
		exit(1)

def client(ip, port, message):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((ip, port))
	try:
		while True:
			msg=raw_input("$ ")
			if msg == None:
				break
			writemsg(sock, msg)
			msg = readmsg(sock)
			if len(msg)==0:
				break
			print "%s" % msg
	except:
		print "Caught: ", sys.exc_info()[0]
	sock.close()
	print "Quitting client"

if __name__ == '__main__':
	params = sys.argv
	dat = sys.argv[1] if len(sys.argv)>1 else "chumma"
	client('localhost', 9999, dat);

