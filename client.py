import socket

s = socket.socket()
port = 56789

s.connect(('127.0.0.1', port)) # to computer, get info from server

print(s.recv(1024)) # 1024 buffer size
s.close()