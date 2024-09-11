from paramiko import client
import time
from getpass import getpass


cli_cisco = ["show version"]

def executor_command(roteador, comandos, username, password):
    # cria uma instancia do cliente SSH
    ssh_client = client.SSHClient()
    # configura a politica para aceitar as chaves automaticamente
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy()) # usar quando nao precisa validar as chaves SSH
    # ssh_client.load_system_host_keys() # usar quando quer carregar as chaves ja salvas no knowhosts
    # ssh_client.load_host_keys(filename='/home/renato/.ssh/known_hosts') # usar quando for especificar aonde estao as chaves

    # conecta no Router
    ssh_client.connect(hostname=roteador, port=22, username=username, password=password)
    print("conectado com sucesso")

    for cmd in comandos:
        stdin, stdout, stderr = ssh_client.exec_command(cmd)
        print(f"{stdout.read().decode()}")
executor_command("192.168.56.120", cli_cisco, "renato", "asterio")