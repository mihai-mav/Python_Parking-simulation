import socket
from . import variables as myvars


def run_on_click2():
    myvars.flag = 1


def run_on_click():
    ClientMultiSocket = socket.socket()
    print('Waiting for connection response')
    try:
        ClientMultiSocket.connect((myvars.host, myvars.port))
    except socket.error as e:
        print(str(e))
    res = ClientMultiSocket.recv(1024)
    while True:
        if res.decode('utf-8').strip() == "You can come in":
            message = "Coming in"
            ClientMultiSocket.send(str.encode(message))
            res = ClientMultiSocket.recv(1024)
            print(res.decode('utf-8'))
        if myvars.flag == 1:
            message = "Enter"
            ClientMultiSocket.send(str.encode(message))
            res = ClientMultiSocket.recv(1024)
            print(res.decode('utf-8'))
            myvars.flag = 0
