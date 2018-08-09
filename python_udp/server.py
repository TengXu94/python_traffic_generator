from socket import *
import time
import sys
import signal

def signal_handler(sig,frame):
	end_time = time.time()
	print("Data Sent:\t" + str(data_size/1024/1024) + "MB")
	print("Number of Packets:\t" + str(n_packets))
	print("Data Rate: \t" + str(data_size*8/1024/1024/(end_time-start_time)) + "Mbit/s")
	exit(0)

signal.signal(signal.SIGINT, signal_handler)
HOST = '192.168.0.1'
PORT = 23567
BUFSIZE = 2048
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

data_size = 0
n_packets = 0
start_time = time.time()

while True:
	data,ADDR = udpSerSock.recvfrom(BUFSIZE)
	data_size += 1500
	n_packets += 1
udpSerSock.close()
    
    
