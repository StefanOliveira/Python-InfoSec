import socket


ipaddr = input("Digite o endereço do Host: ")

srvports = []
count = 0

while count < 10:
    srvports.append(int(input("Digite a porta a ser verificada: ")))
    count += 1

for srvport in srvports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.07)
    code = client.connect_ex((ipaddr, srvport))

    if code == 0:
        print(str(srvport), " -> Porta Aberta!")
    else:
        print(str(srvport), " -> Porta Fechada!")

print("Scan Finalizado")