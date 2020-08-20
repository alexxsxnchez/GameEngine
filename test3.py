import pygame
from Engine import Engine

class Network:
    def send_controls(self, controls):
        pass
    def receive_state(self):
        return None

class Game:
    def __init__(self):
        screen_width = 640
        screen_height = 480
        size = [screen_width, screen_height]
        self.screen = pygame.display.set_mode(size)
        self.network = Network()
        self.run_game()


    def on_pre_update(self):
        controls = {
                'up': False,
                'left': False,
                'right': False,
                'down': False
        }
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.engine.stop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    controls['up'] = True
                if event.key == pygame.K_a:
                    controls['left'] = True
                if event.key == pygame.K_d:
                    controls['right'] = True
                if event.key == pygame.K_s:
                    controls['down'] = True
        self.network.send_controls(controls)
        state = self.network.receive_state()
        world = self.engine.world
        # update world based off controls (client-side prediction) and state from server


    def draw(self):
        world = self.engine.world
        # draw world


    def setup(self):
        world = self.engine.world


    def run_game(self):
        self.engine = Engine()
        self.setup()
        self.engine.on(Engine.PREUPDATE, self.on_pre_update)
        self.engine.on(Engine.POSTUPDATE, self.draw)
        self.engine.start()


def main():
    pygame.init()
    Game()
    pygame.quit()

if __name__ == '__main__':
    main()
