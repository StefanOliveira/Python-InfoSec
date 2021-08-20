import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.07)

ipaddr = input("Digite o endereço do Host: ")
port = int(input("Digite a porta a ser verificada: "))

code = client.connect_ex((ipaddr, port))

if code == 0:
    print("Porta Aberta!")
else:
    print("Porta Fechada!")
