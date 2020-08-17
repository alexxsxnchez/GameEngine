from Physics.Object import Object
from Physics.Vec2 import Vec2

class AABB(Object):
    def __init__(self, min_x, min_y, max_x, max_y, is_static, world):
        assert min_x < max_x and min_y < max_y
        super().__init__(world, is_static)
        self.width = max_x - min_x
        self.height = max_y - min_y
        self.set_position(min_x, min_y)


    def update(self, delta):
        super().update(delta)
        self.__update_bounds_from_position()


    def intersects_AABB(self, other):
        assert isinstance(other, AABB)
        return self.min_bound.x < other.max_bound.x and \
            self.min_bound.y < other.max_bound.y and \
            self.max_bound.x > other.min_bound.x and \
            self.max_bound.y > other.min_bound.y


    def set_position(self, x, y):
        super().set_position(x, y)
        self.__update_bounds_from_position()


    def __update_bounds_from_position(self):
        self.min_bound = self.position
        self.max_bound = self.position + Vec2(self.width, self.height)
