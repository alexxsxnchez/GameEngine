import time
from Physics.World import World

class Engine:

    def __init__(self, **karg):
        self.__max_FPS = karg.get("max_FPS", 60)
        self.__timestep = 1 / self.__max_FPS
        self.world = World(**karg.get("physics", {}))
        print(self.__timestep)


    def update(self, delta):
        self.world.update(delta)


    def start(self):
        stopped = False
        delta = 0
        prev = time.time()

        while not stopped:
            now = time.time()
            delta += now - prev
            if delta < self.__timestep:
                print("about to sleep")
                time.sleep(self.__timestep)
                continue
            # emit pre update
            print('pre')
            prev = now
            number_of_steps = 0
            while delta >= self.__timestep:
                self.update(self.__timestep)
                delta -= self.__timestep
                number_of_steps += 1
                if number_of_steps > 240:
                    # panic
                    print('panic')
                    self.update(delta)
                    delta = 0
            # emit post update
            print('post')

config = {
    #'max_FPS': 60,
    'physics': {
        'gravity': {
            'x': 0,
            'y': 1
        }
    }
}
engine = Engine(**config)
engine.start()
