import socket

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "created socket object"
client.connect((target_host,target_port))
print "connected to client"
client.send("GET / HTTP/1.1\r\nHost:google.com\r\n\r\n")
print "sending packets"
response = client.recv(4096)
print response
