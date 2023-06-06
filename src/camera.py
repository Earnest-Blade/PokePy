import pygame

class Camera:

    def __init__(self, x, y, width, height, zoom=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.zoom_x = zoom
        self.zoom_y = zoom

    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y += 1
        if keys[pygame.K_DOWN]:
            self.y -= 1
        if keys[pygame.K_LEFT]:
            self.x += 1
        if keys[pygame.K_RIGHT]:
            self.x -= 1