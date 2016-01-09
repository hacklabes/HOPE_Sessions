import threading
import SocketServer

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.connection = self.request
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.nickname = self.request.recv(1024).strip() #first data is the nickname
        self.server.addClient(self)
        print "Client> ", self.server.clients, '\n'

        msg = self.nickname + "<- Connected\n"
        self.server.sendBroadcast(self, msg)
        while True:
            data = self.request.recv(1024)
            if data:
                dt = data.strip().split()
                if len(dt) >= 1:
                    if dt[0] == "\C":
                        msgTo = dt[1]
                        if not msgTo:
                            self.server.list_clients()
                            print "CAPTURE", msgTo ,'\n'
                    elif dt[0] == "\L":
                        #send list of users for the client as request
                        list = reduce(lambda x,y: x + '\n' + y, self.server.clients.keys())
                        self.connection.sendall(list)
                    elif dt[0] == "\E":
                        print "CLOSING CLIENT", '\n'
                        self.server.removeClient(self)
                        break
                    else:
                        msg = self.nickname + "> " + data + '\n'
                        self.server.sendBroadcast(self, msg)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, address, handler):
        self.clients = {}
        SocketServer.TCPServer.__init__(self, address, handler)

    def addClient(self, client):
        self.clients[client.nickname] = client

    def removeClient(self,client):
        del self.clients[client.nickname]

    def nicknameExist(self,client):
        return self.clients.has_key(client.nickname)

    def sendBroadcast(self,client, data):
        for c in self.clients.itervalues():
            if c.nickname != client.nickname:
                print c.nickname
                c.request.sendall(data)


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
