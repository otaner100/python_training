show_output = '''GigabitEthernet0/0         192.168.56.120  YES NVRAM  up                    up
GigabitEthernet0/1         unassigned      YES NVRAM  administratively down down
GigabitEthernet0/2         unassigned      YES NVRAM  administratively down down
GigabitEthernet0/3         unassigned      YES NVRAM  administratively down down
Loopback1                  1.1.1.1         YES manual up                    up
'''

inter_lines = show_output.splitlines()
#print(inter_lines)
for lines in inter_lines:
    interface_detalhes = lines.split()

    if interface_detalhes[1] == "unassigned":
        continue
    else:
        print(f"a interface é {interface_detalhes[0]} e IP {interface_detalhes[1]}")


with open ("output.txt", "r") as output:
    lendo = output.readlines()
    for liness in lendo:
        print("aperte enter")
        if input() == "":
            print(liness)
    output.close()