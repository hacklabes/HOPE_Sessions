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
print "Welcome ", nickname

client_socket = socket.socket()
client_socket.connect(('localhost', 8000))
screen = pygame.display.set_mode([1920,720])

pygame.init()  # Initialize pygame

client_socket.sendall(nickname.strip())


def waitPackages():
    while True:
        try:
            package = client_socket.recv(1024)
            print package
        except Exception:
            print "STOP client thread"
            break


thread.start_new_thread(waitPackages,())
try:
    while True:
        userInput = raw_input(" > ")
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
                raise KeyboardInterrupt
            else:
                client_socket.sendall(userInput);
        else:
            print "Type your message or:"
            print "\C nickname for capture"
            print "\L list all connected"
            print "\E for exit"

except KeyboardInterrupt, SystemExit:
    client_socket.close()
