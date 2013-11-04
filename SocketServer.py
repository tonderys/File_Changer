from Tkinter import *
from time import *
import socket

class SocketServer:
    ip = "localhost"
    port = 5005
    buffer_size = 10

    def __init__(self):
        self.top_window = Tk()
        self.message = Label(self.top_window, text = "")
        self.message.grid(column = 1, row = 1)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((ip, port))
        sock.listen(1)

        conn, addr = sock.listen
        print 'Connection Address:', addr
        while 1:
            data = conn.recv(buffer_size)
            if not data: break
            self.message.config(text = data)
            conn.send(data)
        conn.close()
        
socket = SocketServer()
socket.top_window.mainloop()
