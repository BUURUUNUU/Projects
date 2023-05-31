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
        self.colision_sprites = pygame.sprite.Group()
        self.generate_map()
       
        
    def generate_map(self):
        for row_index, row in enumerate(MAP1):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                if col == "x":
                    Obj("assets/personagem/tile.png", [x, y], [self.all_sprites, self.colision_sprites])
                elif col == "p":
                    Player([x, y], [self.all_sprites], self.colision_sprites)
            
                
    def update(self):
        
        return super().update()


class Player(pygame.sprite.Sprite):
    def __init__(self,pos,  groups, colision_group):
        super().__init__(groups)
        
        self.image = pygame.image.load("assets/personagem/idle.png")
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2()
        self.speed = 6
        self.gravity = 0.8
        self.jump_force = 20
        self.colision_group = colision_group
        self.on_ground = False
        
    def input(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_a]:
            self.direction.x = -1
        elif key[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        if key[pygame.K_SPACE] and self.on_ground:
            self.direction.y = - self.jump_force
            self.on_ground = False
            
            
            
    def y_colision(self):
        for sprite in self.colision_group:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.direction.y = 0
                    self.rect.bottom = sprite.rect.top
                    self.on_ground = True
        
            
        
    def move(self):
        self.rect.x +=self.direction.x * self.speed
            
    def gravity_force(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
        
            
            
    def update(self):
        self.input()
        self.move()
        self.gravity_force()
        self.y_colision()
            
        