import pygame, pytmx

import src.camera as camera

class Map:
    path : str
    width: float
    height: float
    tile_width: float
    tile_height: float

class MapRenderer:

    def __init__(self, path):
        self.tmx_data = pytmx.load_pygame(path)
        self.texture = pygame.Surface((self.tmx_data.width * self.tmx_data.tilewidth, self.tmx_data.height * self.tmx_data.tileheight))
        self.surface_size = (self.texture.get_width(), self.texture.get_height())
    
    def draw(self, window:pygame.Surface, camera:camera.Camera):
        for layer in range(len(self.tmx_data.layers)):
            self.draw_layer(layer)

        blit_texture = pygame.transform.scale(self.texture, (camera.zoom_x * self.surface_size[0], camera.zoom_y * self.surface_size[1]))
        window.blit(blit_texture, (camera.x, camera.y))
    
    def draw_layer(self, layer:int):
        for y in range(self.tmx_data.height):
            for x in range(self.tmx_data.width):
                surface = self.tmx_data.get_tile_image(x, y, layer)
                if surface != None:
                    self.texture.blit(surface, (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))

def gen_map_data(path):
    m = Map()
    

    return m