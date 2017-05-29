#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import socket
import threading

sock = socket.socket()

sock.connect(('localhost', 8000))






class ClockThread(threading.Thread):
	def run(self):
		while True:
			sock.send(raw_input()) 

t = ClockThread()
t.start()

while True:
	data = sock.recv(1024)
	if not  data:
		sock.close()
		break
	else:
		print data
	#time.sleep(1)

