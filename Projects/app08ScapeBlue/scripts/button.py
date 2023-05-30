import pygame
from scripts.text import Text
from scripts.settings import *
class Button():
    def __init__(self, color, x, y, text):
        
        self.display = pygame.display.get_surface( )
        self.color = color
        self.rect = pygame.Rect(x, y, 250, 64)
        
        
        self.text = text
        self.text_color = SECONDARY_COLOR 
        self.text_position = [(x + self.rect.width / 2),(y + self.rect.height /2 )]
        
        self.render = Text("assets/fonts/airstrike.ttf", 40, self.text, self.text_color, self.text_position)
        
    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color  = SECONDARY_COLOR
                self.render.update_text(self.text, PRIMARY_COLOR)
            else:
                self.color = PRIMARY_COLOR
                self.render.update_text(self.text, SECONDARY_COLOR)
    
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                print("game")

            
    def draw(self):
        pygame.draw.rect(self.display, self.color, self.rect)
        self.render.draw_center()