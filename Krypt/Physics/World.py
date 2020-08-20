from Krypt.Physics import Factory
from Krypt.Physics import Object
from Krypt.Physics import Vec2

class World:
    def __init__(self, physics):
        self.objects = []
        self.colliders = []
        self.add = Factory(self)
        gravity = physics.get("gravity", {})
        self.gravity = Vec2(gravity.get('x', 0), gravity.get('y', 0))
        print(f"gravity is {self.gravity}")


    def update(self, delta):
        print("world updating")
        for obj in self.objects:
            obj.update(delta)

        collisions = []
        for collider in self.colliders:
            collisions.extend(collider.find_collisions())
        self.__resolve_collisions(collisions)


    def __resolve_collisions(self, collisions):
        pass
