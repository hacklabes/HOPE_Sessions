import SocketServer
import io
import socket
import struct
import cv2
import threading

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		cur_thread = threading.current_thread()
		response = "{}".format(cur_thread.name)
		print "{} wrote:".format(self.client_address[0])

		while True:
			self.data = self.request.recv(1024)
			if self.data:
				self.dt = self.data.strip()
				if self.dt[0]=="E" and len(self.dt)== 1:
					print "CLOSING CLIENT"
					break
				elif self.dt[0]=="C" and len(self.dt)== 1:
					print "SENDING IMAGE"
					self.ret, self.frame = capture.read()
					self.encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
#					self.frame =  cv2.resize(self.frame, (0,0), fx=0.3, fy=0.3) 
					self.result, self.imgencoded = cv2.imencode('.jpg', self.frame, self.encode_param)
					
					self.stream = io.BytesIO()
					self.stream.write(self.imgencoded)
					self.request.sendall(struct.pack('<L', len(self.stream.getvalue())))
					self.stream.seek(0)
					self.request.sendall(self.stream.read())
				#	self.request.sendall(struct.pack('<L', 0))
				else:
					print self.data


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass

if __name__ == "__main__":
	try:
		# Port 0 means to select an arbitrary unused port
		HOST, PORT = "localhost", 8000

		server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
		ip, port = server.server_address

		# Start a thread with the server -- that thread will then start one
		# more thread for each request
		server_thread = threading.Thread(target=server.serve_forever)
		# Exit the server thread when the main thread terminates
		server_thread.daemon = True
		server_thread.start()
		print "Server loop running in thread:", server_thread.name
		capture = cv2.VideoCapture(0)
		server.serve_forever()
	except KeyboardInterrupt:
		capture.release()
		server.shutdown()
		server.server_close()