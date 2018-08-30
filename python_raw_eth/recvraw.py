from scapy.all import *

def pkt_callback(pkt):
 	pkt.show()


interface = "enp1s0"

packets = sniff(iface=interface, prn=pkt_callback, filter='ether proto 0x7A05', store = 0, timeout=20)


