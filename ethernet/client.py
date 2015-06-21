import socket
import time

while True:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("192.168.0.177", 23))
        #client_socket.connect(("192.168.0.100", 8220))
        #data = "GET SONAR "
        #print 'send to server: ' + data
	client_socket.send("h")
        data = client_socket.recv(2048)
	print data
        #receive = client_socket.recv(2048)
        #print receive
        client_socket.close()
        time.sleep(1)
    except Exception as msg:
        print msg
