import os
'''
print(os.getcwd()) # ver qual diretorio atual
print(len(os.listdir())) # numerar quantidade de diretorios/files
print(os.system("ls"))

file = open("config1.txt", "r") # abre o arquivo em modo leitura
commands = file.readlines() # le linha por linha
for command in commands:
    print(command.strip())
file.close()'''

with open("config2.txt", "a") as file2: # 'w' cria um arquivo 'a' adiciona no arquivo
       file2.write("e\nvc\n")
file2.close()
