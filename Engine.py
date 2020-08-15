import time
from Physics.World import World

class Engine:

    def __init__(self, **karg):
        self.max_FPS = karg.get("max_FPS", 60)
        self.timestep = 1000 / self.max_FPS
        self.world = World()
        print(self.timestep)


    def update(self, timestep):
        self.world.update()


    def start(self):
        stopped = False
        delta = 0
        prev = time.time()
        while not stopped:
            now = time.time()
            delta += now - prev
            if delta < self.timestep:
                time.sleep(self.timestep / 1000)
                continue
            # emit pre update
            print('pre')
            prev = now
            number_of_steps = 0
            while delta >= self.timestep:
                self.update(self.timestep)
                delta -= self.timestep
                number_of_steps += 1
                if number_of_steps > 240:
                    # panic
                    print('panic')
                    self.update(delta)
                    delta = 0
            # emit post update
            print('post')

engine = Engine()
engine.start()
