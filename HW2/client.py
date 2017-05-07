import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 10003

print("host {0} port {1}".format(host, port))

s.connect((host, port))

# request file
req_msg = "GET server.py"
s.send(req_msg.encode('ascii'))
print("Send request message {0}".format(req_msg))

# receive file

msg = s.recv(1024).decode('ascii')

if msg == "found":
    print("File is found at the server side. Now receiving...")

    with open('received_file', 'wb') as f:
        while True:
            data = s.recv(1024)
            if not data:
                break
            f.write(data)
    f.close()

    print("Done receiving!")
else:
    print("File can't be found at the server side")

s.close()
