import socket
import os
'''
pwd - показывает название рабочей директории
ls - показывает содержимое текущей директории
cat <filename> - отправляет содержимое файла
'''

dirname = os.path.join(os.getcwd(), 'docs')

def process(req):
    req = req.split()
    if req[0] == 'pwd':
        return dirname
    elif req[0] == 'ls':
        return '; '.join(os.listdir(dirname))
    elif req[0] == 'mkdir':
        try:
            if not os.path.exists(os.path.join(dirname, req[1])):
                os.makedirs(os.path.join(dirname, req[1]))
                return os.path.join(dirname, req[1])
            else:
                return "aleady exists"
        except:
            return "missing arguments!"
    elif req[0] == 'cat':
        filename = os.path.join(os.getcwd(), 'docs')+file_name
        try:
            f = open(filename, "r")
            msg = f.read()
            return str(msg)
        except:
            return 'bad file request!'
    elif req[0] == 'break':
        return 'break'
    else:
        return 'bad request'


PORT = 6666

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', PORT))
sock.listen()
print("Прослушиваем порт", PORT)

flag = True
while flag:
    conn, addr = sock.accept()
    
    request = conn.recv(1024).decode()
    print(request)
    
    response = process(request)
    conn.send(response.encode())
    if response[0] == 'break':
        flag = False
conn.close()
