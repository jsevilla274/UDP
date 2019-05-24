#UDPServer.py

#UDP (SOCK_DGRAM) is a datagram-based protocol. You send one 
#datagram and get one reply and then the connection terminates.
from socket import socket, SOCK_DGRAM, AF_INET
import random

#Create a UDP socket 
#Notice the use of SOCK_DGRAM for UDP packets
#AF_INET is the Internet address family for IPv4
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print("Waiting for connections")

while True:
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(2048)
    if random.random() < 0.5:
        # Capitalize the message from the client and send
        serverSocket.sendto(message.upper(), address)
        print(message.decode(), address)  # decoding bytes message to string
    else:
        print("packet lost")    # "lose" 50% of received packets

serverSocket.close()


#Configure the server so that it randomly drops packets.
#Include information about how long each response took. This will be the RTT.