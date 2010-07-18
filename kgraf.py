#!/usr/bin/env python
import sys
import socket
from messageformat import *
import pickle

class KGraph:
	def __init__(self, home):
		f = open(home+".init", "r")
		self.cfg = pickle.load(f)

