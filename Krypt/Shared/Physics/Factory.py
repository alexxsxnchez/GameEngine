from Krypt.Shared.Physics import AABB
from Krypt.Shared.Physics import Collider

class Factory:
    def __init__(self, world):
        self.world = world
        self.objects = world.objects
        self.colliders = world.colliders
        self.bounds = world.bounds


    def AABB(self, min_x, min_y, max_x, max_y, is_static=False):
        aabb = AABB(min_x, min_y, max_x, max_y, is_static, self.world)
        self.objects.append(aabb)
        if self.bounds and not is_static:
            self.collider(aabb, self.bounds['left'])
            self.collider(aabb, self.bounds['top'])
            self.collider(aabb, self.bounds['right'])
            self.collider(aabb, self.bounds['bottom'])
        return aabb


    def collider(self, a, b, callback=None, enable_collision=True):
        collider = Collider(a, b, callback=callback, enable_collision=enable_collision)
        self.colliders.append(collider)
        return collider
