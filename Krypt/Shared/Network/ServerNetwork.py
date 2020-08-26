from socket import *
from threading import Thread, Lock
from queue import SimpleQueue

class ServerNetwork:
    def __init__(self, port):
        self.port = port
        self.__socket = None
        self.__thread = None
        self.__running = False
        self.__queue = SimpleQueue()


    def open(self, buffer_size=2048):
        self.__socket = socket(AF_INET, SOCK_DGRAM)
        self.__socket.bind('', self.port)
        self.__running = True
        self.__thread = Thread(target=self.__receive, args=[buffer_size])
        self.__thread.start()


    def __receive(self, buffer_size):
            while self.__running:
                data, client_address = self.__socket.recvfrom(buffer_size)
                self.__queue.put((data, client_address))


    def send_state(self, data, client_address):
        self.__socket.sendto(data, client_address)


    def get_state(self):
        state = []
        while not self.__queue.empty:
            item = self.__queue.get_nowait()
            state.append(item)
        return state


    def close(self):
        self.__running = False
        self.__thread.join()

    