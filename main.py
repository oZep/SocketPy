import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPV4
    print("Socket Succesfully Created")
except socket.error as err:
    print(f'socket creation failed with error {err}')


port = 80

try:
    host_ip = socket.gethostbyname('www.github.com')
except socket.gaierror: # problem with DNS
    print('error resolving the host')
    sys.exit()


# connect to the server

s.connect((host_ip, port))
print(f"Socket has succesfully connected to Github on port == {host_ip}")
