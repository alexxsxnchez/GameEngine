from Krypt.Shared.Physics import Vec2

class Object:


    __counter = 0


    def __init__(self, is_static, world):
        self.id = Object.__counter
        Object.__counter += 1

        self.world = world
        self.is_static = is_static
        self.position = Vec2()
        self.velocity = Vec2()
        self.acceleration = Vec2()
        self.dv = Vec2()


    def update(self, delta):
        if self.is_static:
            return
        self.velocity += (self.acceleration + self.world.gravity) * delta
        self.dv = self.velocity * delta
        self.position += self.dv

        self.__round_values()


    def set_position(self, x, y):
        self.position = Vec2(x, y)


    def set_velocity(self, x, y):
        self.velocity = Vec2(x, y)


    def set_acceleration(self, x, y):
        self.acceleration = Vec2(x, y)


    def __round_values(self):
        self.position = self.position.round()
        self.velocity = self.velocity.round()
        self.acceleration = self.acceleration.round()

