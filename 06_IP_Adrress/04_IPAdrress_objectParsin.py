import ipaddress
from pprint import pprint
import sys
import time
from paramiko import client, ssh_exception
import socket
import datetime
import re

int_pattern = re.compile(r'(\S+)\s+(([\d\.]+)|unassinged)\s+\S+\s+\S+\s+(up|administratively down)\s+(\S+)')

new_cmd = ['show ip int bri']
ip_subnet = ipaddress.IPv4Network(input("Enter subnet to match: "))
def cisco_cmd(hostname, commands, username, password):
    try:
        print(f"connectando no device {hostname}..")
        now = datetime.datetime.now().replace(microsecond=0)
        config_atual = f"{now}_{hostname}.txt"
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, password=password, username=username, port=22, look_for_keys=False, allow_agent=False)

        print(f"Conectado no device {hostname}")
        acesso_device = ssh_client.invoke_shell()
        acesso_device.send("terminal len 0\n")
        with open(config_atual, 'w') as cmd_date:
            for cmd in commands:
                acesso_device.send(f"{cmd}\n")
                time.sleep(1)
                output = acesso_device.recv(65535).decode()
                cmd_date.write(output)
                print(output)
        ssh_client.close()
        
        print("### Parsed Output is ###")
        int_iter = int_pattern.finditer(output)
        int_list = list()
        for intf in int_iter:
            int_dict = dict()
            int_dict['int_name'] = intf.group(1)
            int_dict['ip'] = intf.group(2)
            int_dict['status'] = intf.group(5)
            int_list.append(int_dict)
        pprint(int_list)
        print(f"### Interfaces part of subnet {ip_subnet} IPs ###")
        for intf in int_list:
            try:
                ip = ipaddress.IPv4Address(intf['ip'])
                if ip in ip_subnet:
                    print(intf['int_name', ip])
            except ValueError:
                continue

    except ssh_exception.NoValidConnectionsError:
        print("SSH Port invalid")
    except socket.gaierror:
        print("Check the hostname")
    except ssh_exception.AuthenticationException:
        print("authentic failed")

    except:
        print("Exception occured ")
        print(sys.exc_info())
hosts = ['192.168.56.120', '192.168.56.121']
for i in hosts:
    cisco_cmd(i, new_cmd, 'renato', 'asterio')
    time.sleep(2)