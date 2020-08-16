from Physics.Vec2 import Vec2

class Object:

    __counter = 0


    def __init__(self, engine, is_static):
        self.id = Object.__counter
        Object.__counter += 1

        self.engine = engine
        self.is_static = is_static
        self.position = Vec2()
        self.velocity = Vec2()
        self.acceleration = Vec2()


    def set_position(self, x, y):
        self.position = Vec2(x, y).round()


    def set_velocity(self, x, y):
        self.velocity = Vec2(x, y).round()


    def set_acceleration(self, x, y):
        self.acceleration = Vec2(x, y).round()

