import pygame
from scripts.text import Text
class Button():
    def __init__(self, color, x, y, text):
        
        self.display = pygame.display.get_surface( )
        self.color = color
        self.rect = pygame.Rect(x, y, 250, 64)
        
        
        self.text = text
        
        self.render = Text("assets/fonts/airstrike.ttf", 40, self.text, "black", [x, y])
        
        
        
    def draw(self):
        pygame.draw.rect(self.display, self.color, self.rect)
        self.render.draw()