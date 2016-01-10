import io
import socket
import struct
import sys
import cv2
import numpy as np
import pygame
from threading import Thread
import readline

# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)

try:
    client_socket = socket.socket()
    client_socket.connect(('localhost', 8000))
except Exception as e:
    print e.errno, e.strerror
    sys.exit(0)

print "Welcome to the voyeurChat"
print "Start sending your nickname"
#screen = pygame.display.set_mode([1920,720])
#pygame.init()  # Initialize pygame

while True:
    try:
        nickname = raw_input("Insert Nickname > ")
        if len(nickname.strip()) > 3:
            client_socket.sendall("\N")
            client_socket.sendall(nickname.strip())
            data = client_socket.recv(1024)
            if data.split()[0] == "\N":
                print "The Nickname already exist or it's to short, try again"
            elif data.split()[0] == "OK":
                break
        else:
            print "Nickname must be longer"
    except KeyboardInterrupt:
        sys.exit(0)

def waitPackages():
    while True:
        try:
            data = client_socket.recv(1024)
            if len(data) > 0:
                dt = data.split()
                if dt[0] == "\C":
                    #capture
                    print "CAPTURING"
                else:
                    sys.stdout.write('\r'+' '*(len(readline.get_line_buffer())+2)+'\r')
                    print data
                    sys.stdout.write('> ' + readline.get_line_buffer())
                    sys.stdout.flush()

        except Exception:
            print "STOP client thread"
            break

t = Thread(target = waitPackages)
t.daemon = True
t.start()

while True:
    try:
        userInput = raw_input("> ")
        userInput = userInput.strip()
        if len(userInput) > 0:
            dt = userInput.split()
            if dt[0] == "\C":
                if len(dt) >= 2:
                    nickname = dt[1]
                    print "CAPTURE ", nickname
                    client_socket.sendall("\C")
                    client_socket.sendall(nickname)
                    #----now wait for the IMAGE
                else:
                    print "TYPE \C YourFriendNickname"
            elif dt[0]  == "\E":
                #send disconnection
                client_socket.sendall("\E")
                raise SystemExit
            else:
                client_socket.sendall(userInput);
        else:
            print "\n"
            print "Type your message or:"
            print "\C nickname for capture"
            print "\L list all connected"
            print "\E for exit"
    except KeyboardInterrupt, SystemExit:
        client_socket.close()
