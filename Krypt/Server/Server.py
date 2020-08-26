from Krypt.Shared.Engine import Engine
from Krypt.Shared.Physics import Factory
from Krypt.Shared.Network import ServerNetwork

class Server:
    def __init__(self, user_config):
        defaults = {
            'port': 8000,
            'max_fps': 60,
            'physics': {
                'gravity': {
                    'x': 0,
                    'y': 0
                }
            }
        }
        self.__client_addresses = []
        self.__full_config = {**defaults, **user_config}
        self.__network = ServerNetwork(self.__full_config['port'])
        self.__engine = Engine(self.__full_config['max_fps'], self.__full_config['physics'])
        self.__engine.on(Engine.PREUPDATE, self.__preupdate)
        self.__engine.on(Engine.POSTUPDATE, self.__postupdate)
        self.setup()
        self.start()


    def setup(self):
        pass


    def start(self):
        self.__network.open()
        self.__engine.start()


    def __preupdate(self):
        state = self.__network.get_state()
        for s in state:
            self.__process_state(s)


    def __postupdate(self):
        state = self.get_state()
        for client_address in self.__client_addresses:
            self.__network.send_state(state, client_address)


    def __process_state(self, state):
        pass


    def get_state(self):
        return 0
