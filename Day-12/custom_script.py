with open('Day-12/server.conf','r') as file:
    lines = file.readlines()
with open('Day-12/server.conf','w') as file:
    for line in lines:
        if 'MAX_CONNECTIONS' in line:
            file.write(f"MAX_CONNECTIONS = 800 \n")
        else:
            file.write(line)


