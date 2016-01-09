import io
import socket
import struct
import sys
import cv2
import numpy as np
import pygame
import thread


# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)

if len(sys.argv) == 1:
    print "Please add you nickname as argument"
    sys.exit(0)

nickname = str(sys.argv[1])

client_socket = socket.socket()
client_socket.connect(('localhost', 8000))
client_socket.sendall(nickname.strip())
data = client_socket.recv(1024)

if data.split()[0] == "\N":
    print "The Nickname already exist, try again"
    client_socket.close()
    sys.exit(0)

print "Welcome ", nickname
screen = pygame.display.set_mode([1920,720])
pygame.init()  # Initialize pygame

def waitPackages():
    while True:
        try:
            data = client_socket.recv(1024)
            if data !='':
                dt = data.split()
                if dt[0] == "\C":
                    #capture
                    print "CAPTURING"
                else:
                    print data
        except Exception, SystemExit:
            print "STOP client thread"

thread.start_new_thread(waitPackages,())
try:
    while True:
        userInput = raw_input("> ")
        if userInput != '':
            dt = userInput.split()
            if dt[0] == "\C":
                if len(dt) >= 2:
                    msgTo = dt[1]
                    print "CAPTURE ", msgTo
                    client_socket.sendall("\C "+ msgTo)
                    #----now wait for the IMAGE
                else:
                    print "TYPE \C YourFriendNickname"
            elif dt[0]  == "\E":
                client_socket.sendall("\E")
                raise SystemExit
            else:
                client_socket.sendall(userInput);
        else:
            print "Type your message or:"
            print "\C nickname for capture"
            print "\L list all connected"
            print "\E for exit"

except KeyboardInterrupt, SystemExit:
    client_socket.close()
