from socket import *
import time
import sys
import signal

def signal_handler(sig, frame):
	end_time = time.time()
	print("Data Sent:\t" + str(data_size/1048576) + "MB") #1024*1024 = 1048576
	print("Number of Packets:\t" + str(n_packets))
	print("Data Rate: \t" +str(data_size*8/1048576/(end_time-start_time)) + "Mbit/s")
	exit(0)

signal.signal(signal.SIGINT, signal_handler)

src = "\x00\x00\x00\x00\x00\x00"
dst = "\x00\x00\x00\x00\x00\x01"
eth_type = "\x7A\x05"
payload = "0" * 1486
interface = "enp1s0"

max_rate = float(sys.argv[1]) / 8 * 1024 * 1024

data_size = 0
n_packets = 0

s = socket(AF_PACKET, SOCK_RAW)
s.bind((interface,0))

start_time = time.time()

while True:
	if(data_size/(time.time()-start_time) < max_rate):
		s.send(src+dst+eth_type+payload)
		data_size += 1500
		n_packets += 1
s.close()

