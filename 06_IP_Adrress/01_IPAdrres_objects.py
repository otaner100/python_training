import ipaddress

ipaddr = ipaddress.ip_address('127.0.0.1')
print(type(ipaddr))
print(ipaddr.version) # ipv4 ou 6
print(ipaddr.max_prefixlen)
print(ipaddr.reverse_pointer) # DNS
print(ipaddr.is_loopback)
