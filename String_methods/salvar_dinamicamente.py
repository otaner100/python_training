from paramiko import client, ssh_exception
import time
import sys
import datetime

with open ("input_commands.txt", "r") as file2:
    comando = file2.readlines()
print(comando)


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

        data_atual = datetime.datetime.now().replace(microsecond=0) # salva na variavel data_atual
        for cmd in enumerate(comando, start=1): # enumera os comando fazendo startar pelo 1 e nao pelo 0
            file_system = f"{data_atual}_{cmd[0]}_{cmd[1]}".replace(' ','_').strip()
            with open (file_system, 'w') as cmd_data:
                device_invokeSSH.send(f"{cmd[1]}\n")
                time.sleep(4)
                output = device_invokeSSH.recv(65535)
                cmd_data.write(output.decode()) # escreve dentro do file salvar_file o show run
                print(output.decode(), end="")
                
    except ssh_exception.AuthenticationException: #importado o erro gerado quando inserimos a senha errada
        print ("erro na autenticação, check as credencias")
    except:
        print("erro detectado")
        print(sys.exc_info())
executor_command("admin", "admin", "192.168.56.120", comando)