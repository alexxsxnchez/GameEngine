import time

from Krypt.Physics import World

class EventEmitter():
    def __init__(self):
        self.callbacks = {}


    def on(self, event, callback):
        if event not in self.callbacks:
            self.callbacks[event] = [callback]
        else:
            self.callbacks[event].append(callback)


    def emit(self, event, *args, **kargs):
        for callback in self.callbacks.get(event, []):
            callback(*args, **kargs)


class Engine(EventEmitter):

    PREUPDATE = 'preupdate'
    POSTUPDATE = 'postupdate'

    def __init__(self, max_fps, physics):
        super().__init__()
        self.__max_fps = max_fps
        self.__timestep = 1 / self.__max_fps
        self.world = World(physics)
        self.__stopped = False


    def update(self, delta):
        self.world.update(delta)


    def start(self):
        delta = 0
        prev = time.time()

        while not self.__stopped:
            now = time.time()
            delta += now - prev
            if delta < self.__timestep:
                print("about to sleep")
                time.sleep(self.__timestep)
                continue
            self.emit(Engine.PREUPDATE)
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
            self.emit(Engine.POSTUPDATE)


    def stop(self):
        self.__stopped = True
