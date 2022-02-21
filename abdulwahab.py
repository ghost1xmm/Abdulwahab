import socket
import sys
import os
os.system ('clear')


print ("\033[1;33mwelcome \033[1;23mwith \033[1;31mmy \033[1;30mtool \033[1;34m^_^")

print ('Enter your DNS or target ')
hostname = input ( )
ip = socket.gethostbyname(hostname)
print ('HOST NAME IS  :' ,hostname, )
print ('TARGET IP IS: ',ip)
