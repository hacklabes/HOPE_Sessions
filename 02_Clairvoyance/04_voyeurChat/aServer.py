import threading
import SocketServer
import io
import struct
import cv2

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def updateInfor(self):
        self.server.clients_info = []
        for client in self.server.clients:
            self.server.clients_info.append(client.info)

    def addClient(self,client):
        print "Add client to the list", client
        self.server.clients.append(client)

    def handle(self):
        print "Clients> ", self.client_address
        while True:
            data = self.request.recv(1024)
            if data:
                dt = data.strip()
                if dt[0]=="E" and len(dt)== 1:
                    print "CLOSING CLIENT"
                    break
                elif dt[0]=="C" and len(dt)== 1:
                    print "SENDING IMAGE"
                    self.server.list_clients()

                    ret, frame = capture.read()
                    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    #                   self.frame =  cv2.resize(self.frame, (0,0), fx=0.3, fy=0.3)
                    result, imgencoded = cv2.imencode('.jpg', frame, encode_param)
                    stream = io.BytesIO()
                    stream.write(imgencoded)
                    self.request.sendall(struct.pack('<L', len(stream.getvalue())))
                    stream.seek(0)
                    self.request.sendall(stream.read())
                    #   self.request.sendall(struct.pack('<L', 0))
                else:
                    print data
    def removeClient(self,client):
        print "Remove client", client
        try:
            self.server.clients.remove(client)
            self.updateInfo()
        except Exception:
            pass


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, address, handler):
        SocketServer.TCPServer.__init__(self, address, handler)
        self.clients = []
        self.clients_info =[]
    def broadcast(self, data):
        for c in self.clients:
            try:
                c.send(data)
            except:
                self.clients.remove(c)

    def list_clients(self):
        return self.clients_info

    def shutdown(self):
        for c in self.clients:
            c.exit_event.set()
        SocketServer.TCPServer.shutdown(self)


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
