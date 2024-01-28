import socket

# Creating the socker object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Host = '192.168.0.196'
host = socket.gethostname();
port = 9999;

# Binding to socket
serversocket.bind(('192.168.0.196', port)); # Host will be replaced/substitued with IP, if changed and not running on host

#Starting TCP listener
serversocket.listen(3);

while True:
    # Starting the connection
    clientsocket,address = serversocket.accept();

    print(f"Received connection from {address}")

    message = 'Hola! Thank you for connecting to the server' + "\r\n";

    clientsocket.send(message.encode('ascii'));

    clientsocket.close();