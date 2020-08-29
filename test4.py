import pygame
import random
from Krypt.Client import Game, Scene
from Krypt.Shared.Network import ClientNetwork

class MyScene(Scene):
    def __init__(self):
        self.controls = {
            'up': False,
            'left': False,
            'right': False,
            'down': False,
            'restart': False
        }
        self.h = False
        self.player = None
        self.network = ClientNetwork('', 2000)


    def preload(self):
        print("preloading")
        self.load('assets/bomb.png', key='bomb', alpha=True)


    def setup(self):
        print("setting up scene")
        self.player = self.factory.sprite(10, 10, 50, 50, 'bomb', has_physics=True)
        #background = pygame.Surface()
        def f():
            print("collided")
        def remove():
            pass

        for _ in range(1, 10):
            x = random.randint(0, 600)
            y = random.randint(0, 400)
            wall = self.factory.sprite(x, y, 40, 40, 'bomb', has_physics=True, is_static=True)
            self.factory.collider(self.player, wall, f, should_resolve=False)


    def update(self):
        #print("updating scene")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.controls['up'] = True
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.controls['left'] = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.controls['right'] = True
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.controls['down'] = True
                if event.key == pygame.K_n:
                    self.controls['restart'] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.controls['up'] = False
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.controls['left'] = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.controls['right'] = False
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.controls['down'] = False
                if event.key == pygame.K_n:
                    self.controls['restart'] = False
        if self.h:
            for entry in self.controls.items():
                pass
                #print(f"{entry[0]} : {entry[1]}")
        if self.controls['up']:
            self.player.set_velocity(0, -100)
        elif self.controls['down']:
            self.player.set_velocity(0, 100)
        elif self.controls['left']:
            self.player.set_velocity(-100, 0)
        elif self.controls['right']:
            self.player.set_velocity(100, 0)
        else:
            self.player.set_velocity(0, 0)
        if self.controls['restart']:
            self.change_scene(MyScene())


def main():
    config = {
        'scene': MyScene(),
        'width': 1080,
        'height': 720
    }
    Game(config)


if __name__ == '__main__':
    main()
