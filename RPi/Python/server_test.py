# server_test.py
# Tests creating a udp server in python
# Michael Kukar 2016

# REFERENCE https://pymotw.com/2/socket/udp.html

import socket

myPortNum = 8675

# BASED ON UDP (DATAGRAM)

# creates socket to listen on
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# binds the socket to our random port number on our local IP
server_address = ('localhost', myPortNum)
print("Starting up on port " + str(myPortNum))
sock.bind(server_address)

# loops forever and just displays the message it receives
while True:
    data, address = sock.recvfrom(4096)
    print("Received " + str(data) + " from " + str(address))
    if data:
        print("Sending back confirmation message...")
        sent = sock.sendto("Message received.", address)