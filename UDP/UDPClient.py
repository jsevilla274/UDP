#UDPClient.py

from socket import socket, SOCK_DGRAM, AF_INET, timeout
import time

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)    # sets timeout to 1 second
message = input('Input lowercase sentence: ').encode()
RTT = 0
try:
    # send packet to server
    RTT = int(round(time.time() * 1000))    # start time
    clientSocket.sendto(message, (serverName, serverPort))

    # get response from server
    modifiedMessage, addr = clientSocket.recvfrom(2048)
    RTT = int(round(time.time() * 1000)) - RTT    # end time - start time (i.e. RTT in ms)
    print(modifiedMessage.decode(), addr, "\nRTT: " + str(RTT) + "ms");
    clientSocket.close()
except timeout:
    print("Error: Response timeout")


#Allow the client to give up if no response has been received within 1 second.