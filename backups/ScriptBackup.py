import paramiko
import os
from datetime import datetime
import re
import tkinter as tk
from tkinter import ttk

def fwfortigate():
    router_username = "renato"
    router_password = "asterio"
    caminho = []
    todosips_falhados = []
    ips_falhados_autenticacao = []
    ips_falhados_SSH = []

    # Verifique se o arquivo swcisco.txt existe
    file_path = "fortinetFortigate.txt"
    if not os.path.exists(file_path):
        print(f"Erro: O arquivo {file_path} não foi encontrado.")
        exit(1)

    with open(file_path) as f:
        for IP in f:
            IP = IP.strip()
            if IP:
                print("Configurando o sw: " + IP)
                ssh = paramiko.SSHClient()

                # Load SSH host keys.
                ssh.load_system_host_keys()
                # Add SSH host key automatically if needed.
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try:
                    # Connect to router using username/password authentication.
                    ssh.connect(IP, 
                                username=router_username, 
                                password=router_password,
                                look_for_keys=False)

                    # Run command.
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("show full")

                    output = ssh_stdout.readlines()
                    # Close connection.
                    ssh.close()
                    def slugify(value):
                        value = re.sub(r'[^\w\s-]', '', value.upper())
                        return re.sub(r'[-\s]+', '-', value).strip('-_')

                    # Analyze show ip route output
                    hostname = "unknown"
                    for line in output:
                        if line.startswith("    set hostname "):
                            hostname = line.split()[2].strip()
                            hostname = slugify(hostname)
                            break
                    data_atual = datetime.now().strftime("%Y-%m-%d")
                    directory = f'/home/renato/python_demo/backups/{data_atual}'
                    os.makedirs(directory, exist_ok=True)  # Cria a pasta se não existir
                    output_filename = os.path.join(directory, f"{hostname}_{data_atual}.txt")
                    with open(output_filename, 'w') as file:
                        file.writelines(output)
                    # Escrevendo a saída em um arquivo com o nome do hostname
                    print(f"Backup salvo em {output_filename}")
                    if len(caminho) < 1:
                        caminho.append(directory)
                except paramiko.AuthenticationException:
                    print(f"Falha na autenticação para {IP}")
                    todosips_falhados.append(IP)
                    ips_falhados_autenticacao.append(IP)
                except paramiko.SSHException as sshException:
                    print(f"Erro no SSH para {IP}: {sshException}")
                    todosips_falhados.append(IP)
                    ips_falhados_SSH.append(IP)
                except Exception as e:
                    print(f"Ocorreu um erro ao conectar ao {IP}: {e}")
                    todosips_falhados.append(IP)

    # Verifique se há IPs que falharam e escreva-os em um arquivo na pasta "erros"
    if todosips_falhados:
        error_directory = f'/home/renato/python_demo/backups/{data_atual}/erros/'
        os.makedirs(error_directory, exist_ok=True)  # Cria a pasta se não existir
        error_log_filename = os.path.join(error_directory, f"errors_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
        with open(error_log_filename, 'w') as error_file:
            for ip in todosips_falhados:
                error_file.write(f"{ip}\n")
        print(f"IPs com falhas foram registrados em {error_log_filename}")
    ips_falhados_SSH_str = '\n'.join(ips_falhados_SSH)
    result_label_SSH["text"] = ips_falhados_SSH_str
    ips_falhados_autenticacao_str = '\n'.join(ips_falhados_autenticacao)
    result_label_autenticacao["text"] = ips_falhados_autenticacao_str
    ips_falhados_str = '\n'.join(todosips_falhados)
    result_label["text"] = ips_falhados_str
    caminho_str = '\n'.join(caminho)
    result_caminho["text"] = caminho_str
def rtcisco():
    router_username = "renato"
    router_password = "asterio"
    caminho = []
    todosips_falhados = []
    ips_falhados_autenticacao = []
    ips_falhados_SSH = []

    # Verifique se o arquivo swcisco.txt existe
    file_path = "roteadorCiscoASA.txt"
    if not os.path.exists(file_path):
        print(f"Erro: O arquivo {file_path} não foi encontrado.")
        exit(1)

    with open(file_path) as f:
        for IP in f:
            IP = IP.strip()
            if IP:
                print("Configurando o sw: " + IP)
                ssh = paramiko.SSHClient()

                # Load SSH host keys.
                ssh.load_system_host_keys()
                # Add SSH host key automatically if needed.
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try:
                    # Connect to router using username/password authentication.
                    ssh.connect(IP, 
                                username=router_username, 
                                password=router_password,
                                look_for_keys=False)

                    # Run command.
                    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("show run")

                    output = ssh_stdout.readlines()
                    # Close connection.
                    ssh.close()
                    def slugify(value):
                        value = re.sub(r'[^\w\s-]', '', value.upper())
                        return re.sub(r'[-\s]+', '-', value).strip('-_')

                    # Analyze show ip route output
                    hostname = "unknown"
                    for line in output:
                        if line.startswith("hostname "):
                            hostname = line.split()[1].strip()
                            hostname = slugify(hostname)
                            break
                    data_atual = datetime.now().strftime("%Y-%m-%d")
                    directory = f'/home/renato/python_demo/backups/{data_atual}'
                    os.makedirs(directory, exist_ok=True)  # Cria a pasta se não existir
                    output_filename = os.path.join(directory, f"{hostname}_{data_atual}.txt")
                    with open(output_filename, 'w') as file:
                        file.writelines(output)
                    # Escrevendo a saída em um arquivo com o nome do hostname
                    print(f"Backup salvo em {output_filename}")
                    if len(caminho) < 1:
                        caminho.append(directory)
                except paramiko.AuthenticationException:
                    print(f"Falha na autenticação para {IP}")
                    todosips_falhados.append(IP)
                    ips_falhados_autenticacao.append(IP)
                except paramiko.SSHException as sshException:
                    print(f"Erro no SSH para {IP}: {sshException}")
                    todosips_falhados.append(IP)
                    ips_falhados_SSH.append(IP)
                except Exception as e:
                    print(f"Ocorreu um erro ao conectar ao {IP}: {e}")
                    todosips_falhados.append(IP)

    # Verifique se há IPs que falharam e escreva-os em um arquivo na pasta "erros"
    if todosips_falhados:
        error_directory = f'/home/renato/python_demo/backups/{data_atual}/erros/'
        os.makedirs(error_directory, exist_ok=True)  # Cria a pasta se não existir
        error_log_filename = os.path.join(error_directory, f"errors_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
        with open(error_log_filename, 'w') as error_file:
            for ip in todosips_falhados:
                error_file.write(f"{ip}\n")
        print(f"IPs com falhas foram registrados em {error_log_filename}")
    ips_falhados_SSH_str = '\n'.join(ips_falhados_SSH)
    result_label_SSH["text"] = ips_falhados_SSH_str
    ips_falhados_autenticacao_str = '\n'.join(ips_falhados_autenticacao)
    result_label_autenticacao["text"] = ips_falhados_autenticacao_str
    ips_falhados_str = '\n'.join(todosips_falhados)
    result_label["text"] = ips_falhados_str
    caminho_str = '\n'.join(caminho)
    result_caminho["text"] = caminho_str
app = tk.Tk()
app.title("Backup Automático")

# Definir estilos
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TLabel', font=('Helvetica', 12), padding=10)

# Usar frames para organizar
frame_buttons = ttk.Frame(app)
frame_buttons.pack(pady=20)

frame_results = ttk.Frame(app)
frame_results.pack(pady=20)

backupfwfortigate_button = ttk.Button(frame_buttons, text="BKP Firewall Fortigate", command=fwfortigate)
backupfwfortigate_button.pack(side=tk.LEFT, padx=10)
backupfwcisco_button = ttk.Button(frame_buttons, text="BKP Roteador Cisco", command=rtcisco)
backupfwcisco_button.pack(side=tk.LEFT, padx=10)

mensagemcaminho = ttk.Label(frame_results, text=("caminho: "))
mensagemcaminho.pack(pady=10)
result_caminho = ttk.Label(frame_results, text="", background="white", relief="sunken", anchor="w", width=50)
result_caminho.pack(pady=10, fill=tk.X)

mensagematutenticacao = ttk.Label(frame_results, text="Falha na autenticação para IPs: ")
mensagematutenticacao.pack(pady=10)
result_label_autenticacao = ttk.Label(frame_results, text="", background="white", relief="sunken", anchor="w", width=50)
result_label_autenticacao.pack(pady=10, fill=tk.X)

mensagemSSH = ttk.Label(frame_results, text="Erro no SSH para IPs: ")
mensagemSSH.pack(pady=10)
result_label_SSH = ttk.Label(frame_results, text="", background="white", relief="sunken", anchor="w", width=50)
result_label_SSH.pack(pady=10, fill=tk.X)

mensagel_label = ttk.Label(frame_results, text="Falha no backup dos IPs:")
mensagel_label.pack(pady=10)
result_label = ttk.Label(frame_results, text="", background="white", relief="sunken", anchor="w", width=50)
result_label.pack(pady=10, fill=tk.X)

app.mainloop()