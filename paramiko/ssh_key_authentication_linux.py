from paramiko import client, RSAKey
import time
from getpass import getpass


cli_cisco = ["show version"]
ask_pass = getpass("digita a senha da Private Key: ")
key_filename = RSAKey.from_private_key_file(filename="/home/renato/.ssh/02_with_encry", password=ask_pass) # variavel que busca a localização do file da key privada (nao publica) e
# aplica o getpass para digitar a senha para liberar a troca de chaves que no caso é 1234

def executor_command(roteador, comandos, username, password):
    # cria uma instancia do cliente SSH
    ssh_client = client.SSHClient()
    # configura a politica para aceitar as chaves automaticamente
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy()) # usar quando nao precisa validar as chaves SSH
    # conecta no Router
    ssh_client.connect(hostname=roteador, port=22, username=username,
                       look_for_keys=True, 
                       allow_agent=True, 
                       pkey=key_filename) # tirar o password
    print("conectado com sucesso")

    for cmd in comandos:
        stdin, stdout, stderr = ssh_client.exec_command(cmd)
        print(f"{stdout.read().decode()}")
executor_command("192.168.56.120", cli_cisco, "renato") # tirar o password