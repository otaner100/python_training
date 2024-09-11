import ipaddress

ipnet = ipaddress.ip_network('192.168.1.0/29')
print(type(ipnet))
print(ipnet.broadcast_address)
print(ipnet.network_address)
print(ipnet.netmask)
print(ipnet.num_addresses)
print(ipnet.hostmask)
print(ipnet.exploded)
print(ipnet.max_prefixlen)

for ip in ipnet.hosts():
    print(ip)