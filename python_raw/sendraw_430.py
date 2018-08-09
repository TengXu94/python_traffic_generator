from socket import *
import time
import sys
import signal
import struct

def signal_handler(sig, frame):
	end_time = time.time()
	print("Data Sent:\t" + str(data_size/1048576) + "MB") #1024*1024 = 1048576
	print("Number of Packets:\t" + str(n_packets))
	print("Data Rate: \t" +str(data_size*8/1048576/(end_time-start_time)) + "Mbit/s")
	print("Time: \t" + str(end_time-start_time))
	exit(0)

signal.signal(signal.SIGINT, signal_handler)

addr = "\x00\x00\x00\x00\x00\x00" +  "\x00\x00\x00\x00\x00\x01" + "\x7A\x05"
i
payload = "0" * 411
interface = "enp1s0"

max_rate = 2150000 #bytes/s

seq_numbers = map(lambda x: struct.pack('<L',x), list(range(0,100000)))

data_size = 0
n_packets = 0

s = socket(AF_PACKET, SOCK_RAW)
s.bind((interface,0))

start_time = time.time()
while n_packets < 100000:
	if(data_size/(time.time()-start_time) < max_rate):
		s.send(addr+seq_numbers[n_packets]+payload)
		data_size += 430
		n_packets += 1
end_time = time.time()
s.close()
print("Data Sent: \t" +str(data_size/1048576) + "MB")
print("Number of Packets:\t" + str(n_packets))
print("Data Rate: \t" + str(data_size*8/1048576/(end_time-start_time)) + "Mbit/s")
print("Time : \t" + str(end_time - start_time))
