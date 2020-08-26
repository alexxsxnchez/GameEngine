from socket import *

class ClientNetwork:
    def __init__(self, server_ip, port):
        self.server_address = (server_ip, port)
        self.socket = None


    def parse_data(self, data):
        """
        Users should override this method
        """
        pass


    def receive_state(self):
        return 0


    def send_state(self):
        pass


    def __receive(self, buffer_size=2048):
        data, server_address = self.socket.recvfrom(buffer_size)
        if server_address != self.server_address:
            print("received data from unexpected address")
            return None
        return data


    def __send(self, data):
        self.socket.sendto(data, self.server_address)


    def open(self):
        self.socket = socket(AF_INET, SOCK_DGRAM)


    def close(self):
        self.socket.close()
