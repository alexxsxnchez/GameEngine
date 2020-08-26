class SpriteManager:
    def __init__(self):
        self.__sprites = {} # id to sprite
        self.__to_draw = set() # id to bool
        self.surface_cache = {} # cache of sprite assets


    def sprites(self):
        return self.__sprites.values()


    def add(self, sprite):
        self.__sprites[sprite.id()] = sprite
        self.__to_draw.add(sprite)


    def remove(self, sprite):
        self.__sprites.pop(sprite.id())
        self.__to_draw.discard(sprite)


    def sprite_updated(self, sprite):
        if sprite.id() in self.__sprites:
            self.__to_draw.add(sprite)


    def clear_updated(self):
        self.__to_draw.clear()


    def get_sprites_to_draw(self):
        return self.__to_draw
