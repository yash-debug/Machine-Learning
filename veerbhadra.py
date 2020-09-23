import socket 
targetip = "172.16.40.172"
port = 7777
#rec IP+port
#sen IP+port --connect
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                 # for IP           for UDP
s.sendto("hello adhoc nw".encode('ascii'),(targetip,port))
#s.bind((targettip,port))
#while true:
