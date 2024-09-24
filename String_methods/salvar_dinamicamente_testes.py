import datetime

with open ('input_commands.txt') as cmd_commands:
    commands = cmd_commands.readlines()

now = datetime.datetime.now().replace(microsecond=0)
for comando in enumerate(commands, start=1):
    print(now,'_',comando[0], comando[1].strip())