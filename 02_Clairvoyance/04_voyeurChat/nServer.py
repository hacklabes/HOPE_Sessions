import threading
import SocketServer

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def updateInfo(self):
        self.server.clients_info = []
        for client in self.server.clients:
            self.server.clients_info.append(client.info)

    def addClient(self,client):
        print "Add client to the list", client
        self.server.clients.append(client)

    def handle(self):
        nckname = self.request.recv(1024) #first data is the nickname
        self.nickname = nckname.strip()
        self.addClient(self)

        msg = self.nickname + "<- Connected"
        self.server.broadcast(msg)
        print "Client> ", self.client_address
        while True:
            data = self.request.recv(1024)
            if data:
                dt = data.strip().split()

                if len(dt[0]) >= 2:
                    if dt[0] == "\C":
                        self.server.list_clients()
                        print "CAPTURE"
                elif dt[0]=="E" and len(dt)== 1:
                    print "CLOSING CLIENT"
                    self.removeClient(self)
                    break
                else:
                    msg = self.nickame + "> " + data
                    self.server.broadcast(msg)
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
        print "Broadcast> " + data
        for c in self.clients:
            print c
            try:
                c.sendall(data)
            except:
                self.clients.remove(c)

    def list_clients(self):
        return self.clients_info


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
    server.serve_forever()

except KeyboardInterrupt:
    server.shutdown()
    server.server_close()
