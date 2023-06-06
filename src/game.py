import pygame

import src.map as map
import src.camera as camera

class Game:

    def __init__(self):
        self.clock = None
        self.window = None
        self.running = False

        self.map_manager = None
        self.game_camera = None
        self.delta_time = 0

    def init(self, width, height, title):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((width, height))
        self.window.fill((255, 255, 255))
        self.running = False

        self.game_camera = camera.Camera(0, 0, width, height, zoom=2)

        # Map loading
        load_map = map.Map()
        load_map.width = 4
        
        self.map_manager = map.MapRenderer("assets/maps/Jadielle.tmx")

        pygame.display.set_caption(title)

    def run(self):
        self.running = True

        
        while self.running:
            self.clock.tick(60)
            self.window.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop(0)

            self.game_camera.update()
            self.map_manager.draw(self.window, self.game_camera)

            pygame.display.flip()
        
        pygame.quit()
    
    def stop(self):
        self.running = False
        


