class Network:
    def __init__(self, server_ip, port):
        self.server_address = (server_ip, port)


    def parse_data(self, data):
        """
        Users should override this method
        """
        pass


    def receive_state(self):
        return 0


    def send_state(self):
        pass