import pygame
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.text import Text
from scripts.settings import *
from scripts.animatedbg import AnimatedBg

class GameOver(Scene):

    def __init__(self):
        super().__init__()
        
        self.bg = AnimatedBg("assets/menu/bg.png", [0 ,0], [0, -640], [self.all_sprites])  
        self.title = Text("assets/fonts/font_1.ttf", 50, "Game Over", "white", [350, 300])
        
        
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False
        return super().events(event)
        
    def update(self):
        
        
        self.bg.update()
        self.title.drawFade()
       
        return super().update()
    

        