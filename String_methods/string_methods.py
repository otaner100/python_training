username = "admin"

# name = input("digite o nome do usuario: ").casefold().strip().replace(" ","") #casefold tudo em minusculo, strip remove os espaços, replace remove os espaços entre letras

# if name == username:
#     print(f"o user {name} matched")
# else:
#     print("no matched")

# '''find'''
# print(username.find("a")) # procura o index

# '''is decimal'''
# um_numero = '\u001020'
# print(um_numero.isdecimal())

# '''is identifier''' # should not start with number
# username = "1admin"
# print(username.isidentifier())

# '''printable''' # nao pode ter carater diferentes
# username = "1admin\nrenato"
# print(username.isprintable())

'''join''' # especifica oq sera a jncao da lista
list1 = ["renato", "asterio", "lima"]
print(' '.join(list1))

'''ljust''' # adiciona 7 espaçoes entre abc e tudo bem
print("abc".ljust(7), "tudo bem")

'''maketrans''' # substitui as letras
message = "ola mundo"
trans = message.maketrans("o", "k")
print(message.translate(trans))

'''partition''' # particiona a string em lista
string = "como voce vai? tudo bem"
print(string.partition("voce"))

'''replace''' # susbtitui as palavras
sub = "estou lendo o livro"
print(sub.replace("livro", "caderno"))

'''split''' # transforma string em lista

users = "renato, amanda, ricardo"
users_list = users.split(", ")
for user in users_list:
    print(user)

'''splitlines''' # trasnforma lista em string
print("renato\namanda\nricardo".splitlines())

'''zfill''' #adciona o necessario para preencher 
print("ola".zfill(5))