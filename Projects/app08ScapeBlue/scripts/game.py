import random
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text

class Game(Scene):

    def __init__(self):
        super().__init__()
        
        self.generate_map()
        
    def generate_map(self):
        for row_index, row in enumerate(MAP1):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                if col == "x":
                    Obj("assets/personagem/tile.png", [x, y], [self.all_sprites])
                elif col == "p":
                    Player([x, y], [self.all_sprites])
            
                
    def update(self):
        
        return super().update()


class Player(pygame.sprite.Sprite):
    def __init__(self,pos,  groups):
        super().__init__(groups)
        
        self.image = pygame.image.load("assets/personagem/idle.png")
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2()
        self.speed = 2
        
    def input(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_a]:
            self.direction.x = -1
        elif key[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
            
    def move(self):
        self.rect.x +=self.direction.x * self.speed
            
    def update(self):
        self.input()
        self.move()
            
        