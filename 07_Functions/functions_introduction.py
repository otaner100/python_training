import random
import string

def cred(user, priv):
    senha = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
    return f"usuario: {user}, privilegio {priv} e senha {senha}"

with open ("credenciais.txt", "w") as file:
    file.write(cred('renato', 15)'\n')
    file.write(cred('bia', 7))