import pygame
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text
from scripts.button import Button
import sys
class Menu(Scene):

    def __init__(self):
        super().__init__()
        
        self.bg = AnimatedBg("assets/menu/bg.png", [0, 0], [0, -HEIGHT], [self.all_sprites])
        self.title = Obj("assets/menu/title.png", [340, 200], self.all_sprites)

        self.btn_play = Button("white", 64, 400, "Play", self.next_scene)
        self.btn_quit = Button("white", 64, 500, "Quit", self.quit_game)
        
    def next_scene(self):
        self.active = False
        
    def quit_game(self):
        pygame.quit()
        sys.exit()
        
        
    def events(self, event):
       
                
        self.btn_play.events(event)
        self.btn_quit.events(event)
        return super().events(event)

    def update(self):
        self.bg.update()
        self.btn_play.draw()
        self.btn_quit.draw()
        return super().update()




