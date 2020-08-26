import pygame

class Sprite:

    __counter = 0
    __default_surface = pygame.Surface((1, 1)).fill((0, 0, 0))

    def __init__(self, x, y, width, height, image, manager, physics_body):
        self.__id = Sprite.__counter
        Sprite.__counter += 1
        self.__initial_x = x
        self.__initial_y = y
        self.__manager = manager
        self.body = physics_body
        prescaled_image = self.__manager.surface_cache.get(image, Sprite.__default_surface)
        self.image = pygame.transform.scale(prescaled_image, (width, height))


    def id(self):
        return self.__id


    def set_position(self, x, y):
        self.body.set_position(x, y)
        self.__manager.sprite_updated(self)


    def set_velocity(self, x, y):
        self.body.set_velocity(x, y)
        self.__manager.sprite_updated(self)


    def set_acceleration(self, x, y):
        self.body.set_acceleration(x, y)
        self.__manager.sprite_updated(self)


    def get_position(self):
        x = self.__initial_x
        y = self.__initial_y
        if self.body:
            x = self.body.position.x
            y = self.body.position.y
        return x, y


    def draw(self, screen):
        x, y = self.get_position()
        screen.blit(self.image, (x, y))
