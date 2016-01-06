import io
import socket
import struct
import sys
import cv2
import numpy as np
import pygame


if __name__ == "__main__":
	# Connect a client socket to my_server:8000 (change my_server to the
	# hostname of your server)
	client_socket = socket.socket()
	client_socket.connect(('localhost', 8000))
	screen = pygame.display.set_mode([1920,720])
	pygame.init()  # Initialize pygame
	
	try:
		while True:
			userInput = raw_input(" > ")
				
			if userInput != '':
				if userInput.split()[0] == "C" and len(userInput.split()) == 1:
					print "CAPTURE"
					client_socket.sendall("C")
					img_len = struct.unpack('<L', client_socket.recv(struct.calcsize('<L')))[0]
					if img_len > 0:
						data = ''
						while len(data) < img_len:
							packet = client_socket.recv(img_len-len(data))
							if not packet:
								break
							data += packet

					img_stream = io.BytesIO()
					img_stream.write(data)
					
					#img_stream.write(client_socket.recv(img_len))
					# Rewind the stream, open it as an image with PIL and do some
					# processing on it
					img_stream.seek(0)
					img_array = np.fromstring(img_stream.getvalue(), dtype=np.uint8)
					imgCV = cv2.imdecode(img_array,1)
#					cv2.imshow("SERVER",imgCV)
					screen.fill([0, 0, 0])  # Blank fill the screen
					frame=cv2.cvtColor(imgCV,cv2.COLOR_BGR2RGB)
					frame=np.rot90(frame)
					frame=pygame.surfarray.make_surface(frame) #I think the color error lies in this line

					screen.blit(frame, (0, 0))  # Load new image on screen
					pygame.display.update()  # Update pygame display

				elif userInput.split()[0] == "E" and len(userInput.split()) == 1:
					client_socket.sendall("E");
					sys.exit(0)
				else:
					client_socket.sendall(userInput);
			else:
				print "TYPE SOMETHING or C for capture or E for exit"
				
	except KeyboardInterrupt, SystemExit:
		client_socket.close()