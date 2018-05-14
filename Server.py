# -*- coding: utf-8 -*-

# Abra dois terminais, executo o server.py em um terminal
# Execute o client.py em outro terminal
# ou utilize dois equiamentos diferentes e verifique o IP
# Funciona a grosso modo como um arquivo, mas envia o dado pela rede...

import socket

HOST = ''              # Endereco IP do Servidor, não precisa informar, é do equipamento em uso...
PORT = 5000            # Porta que o Servidor esta

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

while True:
    msg, cliente = udp.recvfrom(1024)
    print (cliente, msg)

udp.close()

