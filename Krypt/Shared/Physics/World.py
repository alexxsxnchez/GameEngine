from Krypt.Shared.Physics import Factory
from Krypt.Shared.Physics import Vec2

class World:
    def __init__(self, physics):
        self.objects = []
        self.colliders = []
        self.add = Factory(self)
        gravity = physics.get("gravity", {})
        self.gravity = Vec2(gravity.get('x', 0), gravity.get('y', 0))
        print(f"gravity is {self.gravity}")


    def remove_object(self, obj):
        self.objects.remove(obj)
        colliders_to_remove = []
        for collider in self.colliders:
            if collider.remove_object(obj):
                colliders_to_remove.append(collider)
        self.colliders = [i for i in self.colliders if i not in colliders_to_remove]


    def update(self, delta):
        #print("world updating")
        for obj in self.objects:
            obj.update(delta)

        collisions = []
        for collider in self.colliders:
            collisions.extend(collider.find_collisions())
        self.__resolve_collisions(collisions)


    def __calculate_penetration(self, a, b):
        overlap_bias = 4
        overlap_y = 0
        # if either object is moving along the y axis
        if a.dv.y != 0 or b.dv.y != 0:
            if a.dv.y > b.dv.y:
                # a must be going down and/or b is going up
                overlap_y = a.max_bound.y - b.min_bound.y
            else:
                # a must be going up and/or b is going down
                overlap_y = a.min_bound.y - b.max_bound.y
            # calculate the maximum possible overlap
            max_overlap_y = abs(a.dv.y - b.dv.y) + overlap_bias
            if abs(overlap_y) > max_overlap_y:
                # the overlap is too large for the amount of distance moved
                overlap_y = 0

        overlap_x = 0
        if a.dv.x != 0 or b.dv.x != 0:
            if a.dv.x > b.dv.x:
                # a must be going right and/or b is going left
                overlap_x = a.max_bound.x - b.min_bound.x
            else:
                # a must be going left and/or b is going right
                overlap_x = a.min_bound.x - b.max_bound.x
            # calculate the maximum possible overlap
            max_overlap_x = abs(a.dv.x - b.dv.x) + overlap_bias
            if abs(overlap_x) > max_overlap_x:
                # the overlap is too large for the amound of distance moved
                overlap_x = 0
        return overlap_x, overlap_y


    def __resolve_collisions(self, collisions):
        for collision in collisions:
            if not collision.should_resolve:
                collision.callback()
                continue
            a = collision.a
            b = collision.b
            penetration_x, penetration_y = self.__calculate_penetration(a, b)
            if penetration_x == 0 and penetration_y == 0:
                continue

            if not a.is_static and not b.is_static:
                penetration_x /= 2
                penetration_y /= 2

            # resolve a
            if not a.is_static:
                x = a.position.x - penetration_x
                y = a.position.y - penetration_y
                a.set_position(x, y)
                x = a.velocity.x
                y = a.velocity.y
                if penetration_x != 0:
                    x = -x
                if penetration_y != 0:
                    y = -y
                a.set_velocity(x, y)

            # resolve b
            if not b.is_static:
                x = b.position.x + penetration_x
                y = b.position.y + penetration_y
                b.set_position(x, y)
                x = b.velocity.x
                y = b.velocity.y
                if penetration_x != 0:
                    x = -x
                if penetration_y != 0:
                    y = -y
                b.set_velocity(x, y)

            # call user-provided callback
            collision.callback()
