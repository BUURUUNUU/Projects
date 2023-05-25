import pygame
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.text import Text
from scripts.settings import *
from scripts.animatedbg import AnimatedBg

class Menu(Scene):

    def __init__(self):
        super().__init__()
        
        self.bg = AnimatedBg("assets/menu/bg.png", [0 ,0], [0, -640], [self.all_sprites])  
        self.title = Text("assets/fonts/font_1.ttf", 50, "SpaceShip", "white", [350, 300])
        self.text_info = Text("assets/fonts/font_1.ttf", 30, "Press start to play", "white", [315, 450])
        
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False
        return super().events(event)
        
    def update(self):
        
        
        self.bg.update()
        self.title.draw()
        self.text_info.drawFade()
        return super().update()
    

