import pygame
from Krypt import Game, Network, Scene, Sprite

class MyScene(Scene):
    def __init__(self):
        self.controls = {
            'up': False,
            'left': False,
            'right': False,
            'down': False
        }
        self.h = False

    def preload(self):
        print("preloading")
        self.load('assets/bomb.png')


    def setup(self):
        print("setting up scene")


    def update(self):
        print("updating scene")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.controls['up'] = True
                if event.key == pygame.K_a:
                    self.controls['left'] = True
                if event.key == pygame.K_d:
                    self.controls['right'] = True
                if event.key == pygame.K_s:
                    self.controls['down'] = True
                self.h = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.controls['up'] = False
                if event.key == pygame.K_a:
                    self.controls['left'] = False
                if event.key == pygame.K_d:
                    self.controls['right'] = False
                if event.key == pygame.K_s:
                    self.controls['down'] = False
        if self.h:
            for entry in self.controls.items():
                print(f"{entry[0]} : {entry[1]}")

def main():
    config = {
        'scene': MyScene()
    }
    Game(config)


if __name__ == '__main__':
    main()
