from paramiko import client, ssh_exception
import time
import sys
import datetime
import difflib

'''comandos = ["show version"]


def executor_command(username, password, roteador, comandos):
    try:
        # cria uma instancia do cliente SSH
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        # conecta no Router
        ssh_client.connect(hostname=roteador, port=22, username=username, password=password, look_for_keys=False, allow_agent=False)
        print("conectado com sucesso")
        device_invokeSSH = ssh_client.invoke_shell()
        device_invokeSSH.send("terminal len 0\n")

        salvar_file = f"show_version1_{roteador}" # cria a variavel salvar_file como o nome do file quando ser salvado
        with open (salvar_file, 'w') as file1: # abre a variavel salvar_file como um file, no modo de escrever w
            for cmd in comandos:
                device_invokeSSH.send(f"{cmd}\n")
                time.sleep(4)
                output = device_invokeSSH.recv(65535)
                file1.write(output.decode()) # escreve dentro do file salvar_file o show run
                print(output.decode(), end="")
                
    except ssh_exception.AuthenticationException: #importado o erro gerado quando inserimos a senha errada
        print ("erro na autenticação, check as credencias")
    except:
        print("erro detectado")
        print(sys.exc_info())
executor_command("admin", "admin", "192.168.56.120", comandos)'''

with open ('show_version_192.168.56.120') as compare1:
    no_modify = compare1.read()
with open ('show_version1_192.168.56.120') as compare2:
    modify = compare2.read()
comparação = difflib.Differ().compare(no_modify.splitlines(), modify.splitlines())

for linha in comparação:
    print(linha)