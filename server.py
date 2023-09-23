import socket


s = socket.socket()
print('socket succesfully created')

port = 56789
s.bind(('', port)) # ip empty so server can listen to other requests on the network
print(f'socket binded to port {port}')


s.listen(5) # 5 connection limit for server to listen to
print('socket is listening')

while True:
    c, addr = s.accept()
    print(f'We got the connection from address {addr}')

    message = ('Thank you for connecting')
    c.send(message.encode()) # need to convert the string into bytes as you can only send btyes not strings
    
    # Telnet does not exist on mac so using netcat as an alternative
    # nc localhost 56789

    c.close()