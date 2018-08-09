from socket import *
import time
import sys
import signal

def signal_handler(sig, frame):
	end_time = time.time()
	print("Data Sent:\t" + str(data_size/1048576) + "MB") #1024*1024 = 1048576
	print("Number of Packets:\t" + str(n_packets))
	print("Data Rate: \t"+ str(data_size*8/1048576/(end_time-start_time)) + "Mbit/s")
	exit(0)

signal.signal(signal.SIGINT, signal_handler)

interface = "enp1s0"

data_size = 0
n_packets = 0

s = socket(AF_PACKET, SOCK_RAW, htons(3))
s.bind((interface,0))

start_time = time.time()

while True:
	response = s.recv(4096)
	if response != None:
		print(response)
		data_size += 70
		n_packets += 1
s.close()

