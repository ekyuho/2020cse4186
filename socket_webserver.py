import socket
import time

with socket.socket() as s:
    host = 'localhost'
    port = 8090

    s.bind((host, port))
    print('socket binded to %d'%(port))
    s.listen()
    con, addr = s.accept()
    with con:
        while True:
            data = con.recv(1024)
            if not data:
                break
            print(data)
            con.sendall(b'HTTP/1.1 200 OK\r\n')
            con.sendall(b'Content-Type: text/html\r\n')
            con.sendall(b'Content-Length: 34\r\n\r\n')
            con.sendall(b'Hello <font color=red>World</font>')
