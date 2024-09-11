import re

# teste_tab_linha = "\nhello \tword"
# print(teste_tab_linha)

with open('show_version_192.168.56.120') as file:
    leia = file.read()
# my_pattern = r'Cisco'
# re_output = re.search(my_pattern, leia)
# print(re_output.group(0))

# my_pattern1 = r"(cisco)\.(com)"
# re_output = re.search(pattern=my_pattern1, string=leia)

# if re_output:
#     print("match found")
#     print(re_output.group(0))
#     print(re_output.group(1))
# else:
#     print("Not found")
#########################################################

'''compile'''
# my_pattern = re.compile(r"C....")
# print(my_pattern.search(string=leia)) # printa o primeiro match 
# print(my_pattern.findall(string=leia)) # printa todos os matchs possiveis
# results = my_pattern.finditer(string=leia) # printa todos mas de forma linear
# for result in results:
#     print(result.span())
#########################################################

'''Validate user input'''
# python3 or python3.10
input1 = input("enter Python version: ").casefold()
my_pattern = re.compile(r"python3(\.10)?$")

match = my_pattern.search(input1)
if match:
    print(f"matched {input1}")
else:
    print("not matched")