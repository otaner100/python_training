from paramiko import client
import time
from getpass import getpass

host = ["192.168.56.120", "192.168.56.121"]
for roteador in host:
    roteador == host
    comandos = ["conf t", "inter lo 2","ip add 2.2.2.2 255.255.255.255", "no shut", "end"]
    username = input("digite o usuario: ")
    if not username:
        username = "renato"
        print(f"o usuario padrão foi usado {username}")
        password = getpass(f"coloque a senha: ") or "asterio"

    def executor_host_ciscoCLI(roteador, comandos):
        # cria uma instancia do cliente SSH
        ssh_client = client.SSHClient()

        # configura a politica para aceitar as chaves automaticamente
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy()) # usar quando nao precisa validar as chaves SSH
       # ssh_client.load_system_host_keys() # usar quando quer carregar as chaves ja salvas no knowhosts
       # ssh_client.load_host_keys(filename='/home/renato/.ssh/known_hosts') # usar quando for especificar aonde estao as chaves

        # conecta no Router
        ssh_client.connect(hostname=roteador, port=22, username=username, password=password)

        print("conectado com sucesso")



        # executa os comandos no router
        router_acess = ssh_client.invoke_shell() #invoca o terminal
        router_acess.send("terminal len 0\n") 
        for cmd in comandos:
            router_acess.send(f"{cmd}\n")
            time.sleep(2)
            output = router_acess.recv(65535)
            print(output.decode(), end='')
        router_acess.send("show run\n")
        time.sleep(5)
        output = router_acess.recv(65535)

        print(output.decode())
        ssh_client.close()
    executor_host_ciscoCLI(roteador, comandos)
    time.sleep(5)