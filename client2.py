import socket
from threading import Thread
from tkinter import *

nickname=input('choose ur nickname')
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address='127.0.0.1'
port=8000
client.connect((ip_address,port))

print('connected with server')

class GUI:
    def _init_(self):
        self.window=Tk()
        self.window.withdraw()
        self.login=Toplevel()
        self.login.title('login')
        self.go=Button(self.login,
                       text='continue',
                       font='helvetica 14 bold',
                       command=lambda:self.goahead(self.entryname.get()))
        
def layout(self,name):
    self.name=name
    self.window.deiconify()
    self.window.title('chatroom')
    self.window.resizable(width=False,height=False)
    self.window.configure(width=470,height=550,bg='#17202A')

def sendbutton(self,msg):
    self.textcons.config(state=DISABLED)
    self.msg=msg
    self.entrymsg.delete(0,END)
    snd=Thread(target=self.write)
    snd.start()

def show_message(self,message):
    self.textcons.config(state=NORMAL)
    self.textcons.insert(END,message+'\n\n')
    self.textcons.config(state=DISABLED)
    self.textcons.see(END)   

def goahead(self,name):
    self.login.destroy()
    self.name=name
    rcv=Thread(target=self.receive)
    rcv.start()

def write(self):
    self.textcons.config(state=DISABLED)
    while True:
        message =(f'{self.name}:{self.msg}')
        client.send(message.encode('utf-8'))
        self.show_message(message)
        break

def receive(self):
    while True:
        try:
            message=client.recv(2048).decode('utf-8')
            if message =='nickname':
                client.send(self.name.encode('utf-8'))
            else:
                self.show_message(message)
        except:
            print('an error occured')
            client.close()
            break

receive_thread=Thread(target=receive)
receive_thread.start()
write_thread=Thread(target=write)
write_thread.start()

g=GUI()