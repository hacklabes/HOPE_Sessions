import threading
import SocketServer
import logging
import struct

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("voyeurChatServer")


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def sendData(self, data):
        print "sendinding ", self
        self.request.sendall(struct.pack('<L', len(data))) #size of my data
        self.request.sendall(data)
        self.request.sendall(struct.pack('<L', 0)) #size of my data

    def receiveData(self):

        size = struct.unpack('<L', self.request.recv(struct.calcsize('<L')))[0]
        if size > 0:
            data = ''
            while len(data) < size:
                packet = self.request.recv(size-len(data))
                if not packet:
                    break
                data += packet
            return data
        return ''


    def handle(self):
        self.connection = self.request
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.nickname = self.ip + ":" + str(self.port)
        self.server.addClient(self)
        log.info("Client connect - %s", self.client_address)
        while True:
            try:
                data = self.receiveData()
                if data.split()[0] == "\N":
                    nn = self.receiveData().strip()
                    if not self.server.nicknameExist(nn) and len(nn) > 3:
                        log.info("Updated nickname - %s", nn)
                        self.server.updateNickname(self, nn)
                        self.sendData("OK") #nickname errr
                        break
                    else:
                        self.sendData("\N")
                        log.info("Error updating nickname")
            except:
                log.info("Error getting nickname")
                break

        msg = self.nickname + "> Connected"
        self.server.sendBroadcast(self, msg)

        while True:
            try:
                data = self.receiveData()
                if data:
                    dt = data.strip().split()
                    if len(dt) > 1:
                        if dt[0] == "\C":
                            nickname = self.receiveData()
                            if self.server.nicknameExist(nickname):
                                log.info("Capture - %s", nickname)
                        elif dt[0] == "\L":
                            #send list of users for the client as request
                            list = "==== Users ====\n"
                            list += reduce(lambda x,y: x + "\n" + y, self.server.clients.keys())
                            list += "\n==============="
                            self.sendData(list)
                        elif dt[0] == "\E":
                            self.server.sendBroadcast(self, self.nickname + "> Disconnected")
                            log.info("Closing Client - %s", self.client_address)
                            self.server.removeClient(self)
                            break
                        else:
                            msg = self.nickname + "> " + data
                            self.server.sendBroadcast(self, msg)
            except Exception:
                log.info("Client connection error")
                break

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, address, handler):
        self.clients = {}
        SocketServer.TCPServer.__init__(self, address, handler)

    def updateNickname(self, client, nickname):
        self.clients[nickname] = self.clients.pop(client.nickname)
        client.nickname = nickname

    def removeClient(self,client):
        del self.clients[client.nickname]

    def nicknameExist(self, nickname):
        return self.clients.has_key(nickname)

    def sendBroadcast(self,client, data):
        for c in self.clients.itervalues():
            if c.nickname != client.nickname:
                c.sendData(data)

    def addClient(self, client):
        if self.nicknameExist(client.nickname):
            return True #send error
        self.clients[client.nickname] = client
        return False #no error



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
    log.info("Server loop running in thread - %s", server_thread.name)
    server.serve_forever()

except KeyboardInterrupt:
    server.shutdown()
    server.server_close()
