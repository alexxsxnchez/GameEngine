class Collision:
        def __init__(self, a, b, callback, enable_collision):
            self.a = a
            self.b = b
            self.callback = callback
            self.enable_collision = enable_collision


class Collider:

    def __init__(self, a, b, callback=None, enable_collision=True):
        self.a = a
        self.b = b
        if not callback:
            def empty(): pass
            callback = empty
        self.callback = callback
        self.enable_collision = enable_collision


    def find_collisions(self):
        collisions = []
        if self.a and self.b:
            if self.a.intersects_AABB(self.b):
                collisions.append(Collision(self.a, self.b, self.callback, self.enable_collision))
        return collisions


    def remove_object(self, obj):
        if obj == a:
            a = None
            return True
        if obj == b:
            b = None
            return True
        return False
