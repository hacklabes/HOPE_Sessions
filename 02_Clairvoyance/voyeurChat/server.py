import io
import socket
import struct
import sys
import cv2
import numpy as np
# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
server_socket = socket.socket()
server_socket.bind(('localhost', 8000))
server_socket.listen(0)

# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('rb')
try:
	# Read the length of the image as a 32-bit unsigned int. If the
	# length is zero, quit the loop
	img_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
	if not img_len:
		sys.exit(0)
	# Construct a stream to hold the image data and read the image
	# data from the connection
	img_stream = io.BytesIO()
	img_stream.write(connection.read(img_len))
	# Rewind the stream, open it as an image with PIL and do some
	# processing on it
	img_stream.seek(0)
	img_array = np.fromstring(img_stream.getvalue(), dtype=np.uint8)
	imgCV = cv2.imdecode(img_array,1)
	cv2.imshow("SERVER",imgCV)
	cv2.waitKey(0)
finally:
	connection.close()
	server_socket.close()
	cv2.destroyAllWindows()
