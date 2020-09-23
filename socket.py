import socket 
ip = "172.16.40.172"
port = 7777
vbshttp=(ip,port)
#rec IP+port
#sen IP+port --connect
#this will be socket of vbshttp protocol
# now we can create UDP socket
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
msg=input("are dada")
msg1=msg.encode('ascii')

#now we can send to server
s.sendto((msg1,vbshttp))
#while true:
