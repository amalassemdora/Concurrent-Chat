"""

@author: Amal Assem Dora

"""
# import socket programming library 
from socket import *
  
# import thread module 
from _thread import *
import threading 
    
# thread function 
# reverse the given string from client 
def receive_thread(c): 
    while True: 
  
        # data received from client 
        x = c.recv(500) 
        print(x.decode('UTF-8'))

def client_thread(c):
    receive=threading.thread(target=receive_thread,arg=(c,))
    receive.start()
    while True:
        c.send(input("server:").encode('UTF-8'))
  
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
host = "127.0.0.1" 
port = 7000
s.bind((host, port)) 

# put the socket into listening mode 
s.listen(5) 

try:
# a forever loop until client wants to exit 
    while True: 
      
        # establish connection with client 
        c, addr = s.accept() 
      
        # lock acquired by client 
        print_lock.acquire() 
        print('Connected to :', addr[0]) 
    
        # Start a new thread and return its identifier 
       start_new_thread(client_thread, (c,)) 
except keyboardInterrupt:
    s.close() 


