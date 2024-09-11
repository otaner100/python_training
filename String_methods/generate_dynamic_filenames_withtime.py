import datetime
with open ("input_commands.txt", "r") as cmd_file:
    comandos = cmd_file.readlines()

agora = datetime.datetime.now().replace(microsecond=0)
for linha in enumerate(comandos, start=1):
    print(f"{agora}_{linha[0]}_{linha[1]}".replace(' ','_').strip())