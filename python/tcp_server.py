import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

# AF_INET uses standard IPv4 addr/hostname.
# SOCK_STREAM = TCP Client.
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Tells the server to start listening.
server.bind((bind_ip,bind_port))
server.listen(5) # 5 = maximum backlog
print "[*] Listening on %s:%d" % (bind_ip, bind_port)

# Performs the RECV() and sends a simple message back to client.
def handle_client(client_socket):
    request = client_sock.recv(1024)
    print "[*] Received: %s" & request
    client_socket.send("ACK!")
    client_socket.close()

while True:
    # Receive the client socket into client variable, the remote connection details
    # into the addr variable. Create a new thread object that points
    # to handle_client function, and pass it the client_object.
    client,addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
