# -*- coding: utf-8 -*-

# Exemplo de socket, para dois programas (jogos) trocarem mensagens
# entre m�quinas diferentes
# Utilizar IP loopback para testar no mesmo equipamento (127.0.0.1 ou localhost)
# Utilizar UDP para jogos, mas h� outras op��es como TCP (que garante a entrega)
# e com Treads para multi usu�rios, consulte a refer�ncia abaixo:
#
# Fonte: https://wiki.python.org.br/SocketBasico
# Fonte: https://docs.python.org/3/library/socket.html
#
# Exemplo de socket com PyGame:  https://gist.github.com/marvin/4286692

import socket

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000         # Porta que o Servidor esta, usar porta > 1024

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

print ('Para sair use CTRL+X\n')

msg = input()
while msg != '\x18':
     udp.sendto (msg.encode(), dest)
     msg = input()

udp.close()