#!/usr/bin/env python
import sys
import socket
from struct import pack,unpack

def writemsg(sock, msg):
	msg = "feed"+pack('L',len(msg))+msg+"feed"
	sock.send(msg)

def readmsg(sock):
	feed = sock.recv(4)
	if len(feed)==0:
		return None
	if feed != "feed":
		raise TypeError('Wrong StartSentinel: '+str(len(feed)))
	l = unpack('L',sock.recv(4))[0]
	if (l==0):
		raise TypeError('Message of length zero from socket')
	msg = sock.recv(l)
	feed = sock.recv(4)
	if feed != "feed":
		raise TypeError('Wrong EndSentinel: '+feed)
	return msg

