import socket
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 10003

print("host {0} port {1}".format(host, port))

server_socket.bind((host, port))

server_socket.listen(5)

while True:
    # establish a connection
    client_socket, addr = server_socket.accept()

    print("Got a connection from %s" % str(addr))

    # look for file
    req_msg = client_socket.recv(1024).decode('ascii')
    print(req_msg)

    split = req_msg.split(" ")
    print(split)

    print("Looking for file {0}".format(split[1]))

    isFound = False
    for filename in os.listdir("."):
        if filename == split[1]:
            print("Requested file is found!")
            isFound = True

            # send file
            client_socket.send("found".encode('ascii'))

            f = open(filename, 'rb')
            l = f.read(1024)
            while l:
                client_socket.send(l)
                l = f.read(1024)
            f.close()

            break

    if isFound is False:
        print("Requested file is not found!")
        client_socket.send("error".encode('ascii'))

    client_socket.close()
