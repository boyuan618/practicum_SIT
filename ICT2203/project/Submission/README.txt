Configured Network Defences
=======================


Definitions
========
1. Enable port security - Prevent MAC flooding


2. Shut down all unused ports, move to unused VLAN and remove the VLAN - Prevent Switch spoof / VLAN hopping


3. Ensure native VLAN is not used for any access ports or force all traffic to be tagged - Prevent Double tagging attack


4. BPDU guard / Root guard - Prevent STP attack


5. Disable CDP except on VoIP ports which require it - Prevent CDP sniffing


6. DHCP Snooping & Deep packet inspection - Prevent DHCP starvation & Rogue DHCP / DNS server


7. Enable Dynamic ARP Inspection (DAI) - Prevent ARP poisoning (MITM)


8. Enable IP source guard - Prevent IP / MAC spoofing


9. ACL configuration - Mitigate DOS attacks, deny network probing & prevent common attacks on web server like XSS, SQL Injection, etc


10. Filter our own allocated external IP and all internal IPs (spoofed) from entering edge router - Prevent Reflection / Amplification DOS attack


11. ACL Filter FO=1 - Prevent Tiny fragment attack / Overlapping fragment attack


12. NTP Authentication - Identify secure servers from unauthorised or illegal servers


Devices
======
ASA Firewall - (9) (12)


Router 1 - (5) (9) (10) (11) (12)


Router 2 - (5) (12)


Switch 1 - (1) (2) (3) (4) (5) (12)


Switch 2 - (1) (2) (3) (4) (5) (12)


Switch 3 - (1) (2) (3) (4) (5) (6) (7) (8) (12)


Switch 4 - (1) (2) (3) (4) (5) (6) (7) (8) (12)


Switch 5 - (1) (2) (3) (4) (5) (12)