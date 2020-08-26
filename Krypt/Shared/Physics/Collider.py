class Collision:
        def __init__(self, a, b, callback, should_resolve):
            self.a = a
            self.b = b
            self.callback = callback
            self.should_resolve = should_resolve

class Collider:

    def __init__(self, a, b, callback=None, should_resolve=True):
        self.a = a
        self.b = b
        if not callback:
            def empty(): pass
            callback = empty
        self.callback = callback
        self.should_resolve = should_resolve


    def find_collisions(self):
        collisions = []
        if self.a and self.b:
            if self.a.intersects_AABB(self.b):
                collisions.append(Collision(self.a, self.b, self.callback, self.should_resolve))
        return collisions


    def remove_object(self, obj):
        if obj == a:
            a = None
            return True
        if obj == b:
            b = None
            return True
        return False
