import random
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text
from scripts.player import Player
from scripts.fade import Fade
from scripts.camera import Camera


class Game:
    def __init__(self):
        self.active = True
        self.stage = 0
        self.maps = [MAP0, MAP1, MAP2, MAP3, MAP4, MAP5]#, MAP6, MAP7, MAP8, MAP9, MAP10, MAP11, MAP12]
        self.current_level = Level(self.maps[self.stage])
        
    def events(self, event):
        pass
    
    def draw(self):
        self.current_level.draw()
    
    def update(self):
        if self.current_level.active == False and self.current_level.gameover == False:
                self.stage += 1
                
                
                self.current_level =  Level(self.maps[self.stage])
        elif self.current_level.active == True and self.current_level.gameover == True:
                self.active = False
                
                
        self.current_level.update()
        

class Level:

    def __init__(self, worldmap):
       
        self.display = pygame.display.get_surface()
        self.all_sprites = Camera()
        self.colision_sprites = pygame.sprite.Group()
        self.active = True
        self.gameover = False

        self.fade = Fade(5)
        self.finish = Obj("assets/player/finish.png", [0, 0], self.all_sprites)
       
       
        
        
        self.player = Player([0, 0], [self.all_sprites], self.colision_sprites)
        self.worldmap = worldmap
        
        self.generate_map()
        
        self.hud_ui = Ui()
       
        
    def generate_map(self):
        for row_index, row in enumerate(self.worldmap):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                if col == "X":
                    Obj("assets/player/tile.png", [x, y], [self.all_sprites, self.colision_sprites])
                elif col == "C":
                    self.finish.rect.x = x
                    self.finish.rect.y = y
                
    def events(self, event):
        pass
    
    
    def next_stage(self):
         if self.player.rect.colliderect(self.finish.rect):
            self.active = False
            
    def reset_position(self):
        if self.player.rect.y > HEIGHT:
            self.player.rect.x = 0
            self.player.rect.y = 0
            self.hud_ui.lifes -= 1
            
        if self.hud_ui.lifes <= 0:
            self.gameover = True
                
    def draw(self):
        self.all_sprites.costume_draw(self.player)
        self.hud_ui.draw()
        self.fade.draw()
            
                
    def update(self):
        self.all_sprites.update()
        self.next_stage()
        self.reset_position()
        self.hud_ui.update()
        
        
       
        
        
class Ui:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.ui_group = pygame.sprite.Group()
        
        self.hud1 = Obj("assets/player/idle_0.png", [0, 10], [self.ui_group])
        self.hud2 = Obj("assets/player/idle_0.png", [74, 10], [self.ui_group])
        self.hud3 = Obj("assets/player/idle_0.png", [144, 10], [self.ui_group])
        
        self.lifes = 3
        
    def count_lifes(self):
        if self.lifes == 2:
            self.hud3.kill()
        elif self.lifes == 1:
            self.hud2.kill()
        elif self.lifes == 0:
            self.hud1.kill()
            
        
    def draw(self):
        self.ui_group.draw(self.display)


    def update(self):
        self.count_lifes()

