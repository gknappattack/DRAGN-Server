import socket
import signal
import sys
import os
from _thread import *

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

ServerSocket = socket.socket()
host = '127.0.0.1' # loopback address
#host = '192.168.19.10'
port = 1234
ThreadCount = 0
signal.signal(signal.SIGINT, signal_handler)

host = input('Please enter a host IP address (enter \'DEFAULT\' for loopback, \'HOST\' for host pc iPv4):')
port = input('Please enter a host port (enter \'DEFAULT\' for \'1234\'):')
if host == 'DEFAULT':
    host = '127.0.0.1'
if host == 'HOST':
    host = socket.gethostname()
    #print(host)
    host = socket.gethostbyname(host)
    #print(host)
if port == 'DEFAULT':
    port = 1234
else:
    port = int(port)

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Starting Server on {h}:{p}'.format(h=host, p=port))
print('Waiting for a Connection..')

ServerSocket.listen(5)

def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()
            

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))

