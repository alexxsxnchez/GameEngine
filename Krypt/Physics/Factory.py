from Krypt.Physics import AABB
from Krypt.Physics import Collider

class Factory:
    def __init__(self, world):
        self.world = world
        self.objects = world.objects
        self.colliders = world.colliders


    def AABB(self, min_x=0, min_y=0, max_x=0, max_y=0, is_static=False):
        aabb = AABB(min_x, min_y, max_x, max_y, is_static, self.world)
        self.objects.append(aabb)
        return aabb


    def collider(self, a, b, callback):
        collider = Collider(a, b, callback)
        self.colliders.append(collider)
        return collider
