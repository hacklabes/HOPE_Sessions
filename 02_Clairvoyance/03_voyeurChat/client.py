import io
import socket
import struct
import cv2
# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
client_socket = socket.socket()
client_socket.connect(('localhost', 8000))

capture = cv2.VideoCapture(0)
# Make a file-like object out of the connection
connection = client_socket.makefile('wb')
try:
	ret, frame = capture.read()
	ret, frame = capture.read()
	print ret
	cv2.imshow('frame',frame)
	encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
	result, imgencoded = cv2.imencode('.jpg', frame, encode_param)
	stream = io.BytesIO()
	stream.write(imgencoded)

	connection.write(struct.pack('<L', stream.tell()))
	connection.flush()

	stream.seek(0)
	connection.write(stream.read())
	connection.write(struct.pack('<L', 0))
	cv2.imshow("CLIENT",frame)
	cv2.waitKey(0)
finally:
	connection.close()
	client_socket.close()
	cv2.destroyAllWindows()
