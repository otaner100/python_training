from paramiko import client, ssh_exception
import time
from getpass import getpass
import sys

cli_cisco = ["show version"]
username = "renato"
password = "lima" #senha errada

def executor_command(roteador, comandos):
    try:
        # cria uma instancia do cliente SSH
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        # conecta no Router
        ssh_client.connect(hostname=roteador, port=22, username=username, password=password)
        print("conectado com sucesso")

        for cmd in comandos:
            stdin, stdout, stderr = ssh_client.exec_command(cmd)
            print(f"{stdout.read().decode()}")
    except ssh_exception.AuthenticationException: #importado o erro gerado quando inserimos a senha errada
        print ("erro na autenticação, check as credencias")
    except:
        print("erro detectado")
        print(sys.exc_info())
executor_command("192.168.56.120", cli_cisco)