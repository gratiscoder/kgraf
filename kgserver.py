#!/usr/bin/env python

import socket
import threading
import SocketServer
from messageformat import *

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		mename = threading.currentThread().getName()
		sock = self.request
		try:
			while True:
				msg = readmsg(sock)
				if msg == None:
					print 'thanx for talking to '+mename
					break
				print mename+" got "+msg
				if msg == 'quitser':
					sock.close()
					server.shutdown()
					break
				msg = "%s# %s" % (mename, "d'u say '%s' ? "%msg)
				writemsg(sock, msg)
		except:
			print "Caught: ", sys.exc_info()
			server.shutdown()
		print 'Exiting '+mename

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass

if __name__ == "__main__":
	# Port 0 means to select an arbitrary unused port
	HOST, PORT = "localhost", 9999

	server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)

	# Start a thread with the server -- that thread will then start one
	# more thread for each request
	server_thread = threading.Thread(target=server.serve_forever)
	# Exit the server thread when the main thread terminates
	server_thread.setDaemon(True)
	server_thread.start()
	print "Server loop running in thread:", server_thread.getName()
	server_thread.join()

