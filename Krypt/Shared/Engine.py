import time

class EventEmitter():
    def __init__(self):
        self.callbacks = {}


    def on(self, event, callback, only_once=False):
        value = (callback, only_once)
        if event not in self.callbacks:
            self.callbacks[event] = [value]
        else:
            self.callbacks[event].append(value)


    def emit(self, event, *args, **kargs):
        callbacks = self.callbacks.get(event, [])
        self.callbacks[event] = [callback for callback in callbacks if not callback[1]]
        for callback, _ in callbacks:
            callback(*args, **kargs)


class Engine(EventEmitter):

    PREUPDATE = 'preupdate'
    UPDATE = 'update'
    POSTUPDATE = 'postupdate'
    STOP = 'stop'

    def __init__(self, max_fps):
        super().__init__()
        self.__max_fps = 60
        if max_fps != 0:
            self.__max_fps = max_fps
        self.__timestep = 1 / self.__max_fps
        self.__stopped = False

    def start(self):
        self.__stopped = False
        delta = 0
        prev = time.time()

        while not self.__stopped:
            now = time.time()
            delta += now - prev
            if delta < self.__timestep:
                time.sleep(self.__timestep)
                continue
            self.emit(Engine.PREUPDATE)
            prev = now
            number_of_steps = 0
            while delta >= self.__timestep:
                self.emit(Engine.UPDATE, self.__timestep)
                delta -= self.__timestep
                # print(number_of_steps)
                number_of_steps += 1
                if number_of_steps > 240:
                    # panic
                    print('panic')
                    self.emit(Engine.UPDATE, delta)
                    delta = 0
            self.emit(Engine.POSTUPDATE)
        self.emit(Engine.STOP)


    def stop(self):
        self.__stopped = True
