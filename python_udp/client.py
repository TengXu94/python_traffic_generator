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
ADDR = (HOST,PORT)

max_rate = (1024*1024 * float(sys.argv[1])) / 8 #bytes/s 
msg = str.encode("A") * 1458 # +20B IPv4 Header + 8B UDP header + 14B ETH II header = 1500B

udpCliSock = socket(AF_INET,SOCK_DGRAM)

data_size = 0
n_packets = 0
start_time = time.time()
while True:
	if(data_size/(time.time()-start_time) < max_rate): 
		udpCliSock.sendto(msg,ADDR)
		data_size += 1500
		n_packets += 1
udpCliSock.close()
