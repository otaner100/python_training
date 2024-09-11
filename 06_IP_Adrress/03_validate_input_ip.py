import ipaddress

ip_list = []
while True:
    try:
        ip_input = input(f"\n\n{'~' * 50}\ndigite o IPV4/list/exit: ")
        if ip_input == 'exit':
            print("saindo do loop")
            break
        if ip_input == 'list':
            print(f"lista atual dos IPS: {sorted(ip_list)}")
            continue
        else:
            ip_input = ipaddress.ip_address(ip_input)
        lan_subnet = ipaddress.ip_network("192.168.0.0/24")
        if ip_input not in ip_list:
            if ip_input in lan_subnet:
                ip_list.append(ip_input)
                print("IP adicionado na lista")
            else:
                print("ip invalido na mascara")
        else:

            print("IP ja esta na lista")
    except ValueError:
        print("IP Invalido")