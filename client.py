"""

@author: Amal Assem Dora

"""

# Import socket module 
from socket import *
from _thread import *
import threading
  
 
def thread_receive(s):
    while True:
            x=s.recv(500)
            print(x.decode('UTF-8'))
 

s = socket(AF_INET,SOCK_STREAM) 
# local host IP '127.0.0.1' 
host = "127.0.0.1"
  
# Define the port on which you want to connect 
port = 7000
  
# connect to server on local computer 
s.connect((host,port)) 
  
# messaga received from server 
receive = threading.Thread(target=thread_receive, args=(s,))
receive.start()
while True:
    # message sent to server 
          s.send(input("Client:").encode("UTF-8"))
