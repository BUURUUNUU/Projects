import random
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text
from scripts.player import Player
from scripts.fade import Fade
class Game:

    def __init__(self):
       
        self.display = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.colision_sprites = pygame.sprite.Group()
        self.active = True

        self.fade = Fade(5)
       
       
        
        
        self.player = Player([0, 0], [self.all_sprites], self.colision_sprites)
        
        self.generate_map()
       
        
    def generate_map(self):
        for row_index, row in enumerate(MAP1):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                if col == "x":
                    Obj("assets/player/tile.png", [x, y], [self.all_sprites, self.colision_sprites])
                
                
    def events(self, event):
        pass
                
    def draw(self):
        self.all_sprites.draw(self.display)
            
                
    def update(self):
        self.all_sprites.update()


