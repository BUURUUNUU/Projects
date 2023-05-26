import pygame
from scripts.scene import Scene
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.settings import *

class Game(Scene):

    def __init__(self):
        super().__init__()

        self.bg = AnimatedBg("assets/menu/bg.png", [0 ,0], [0, -640], [self.all_sprites]) 
        self.spaceship =  SpaceShip("assets/nave/player0.png", [450, 500], [self.all_sprites])
        
        self.tick = 0
        
        self.enemy_colision = pygame.sprite.Group()
        
        
        
    def spawn_enemy(self):
        self.tick += 1
        if self.tick > 60:
            self.tick = 0
            Enemy("assets/nave/enemy0.png", [self.spaceship.rect.x, -100], [self.all_sprites, self.enemy_colision])
            
            
    def colision(self):
        for shot in self.spaceship.shots:
            for enemy in self.enemy_colision:
                if shot.rect.colliderect(enemy.rect):
                    shot.kill()
                    enemy.kill()
        
    def update(self):
        self.colision()
        self.spaceship.shots.draw(self.display)
        self.spaceship.shots.update()
        self.bg.update()
        self.spaceship.input()
        self.spawn_enemy()
        return super().update()
    
    
class SpaceShip(Obj):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.direction = pygame.math.Vector2()
        self.speed = 5
        
        
        self.shots = pygame.sprite.Group()
        self.ticks = 0
     

    def input(self):
        
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.direction.y = -1
            
        
        elif key[pygame.K_s]:
             self.direction.y = 1
        
        else:
            self.direction.y = 0
            
            
        if key[pygame.K_a]:
            self.direction.x = -1
            
        
        elif key[pygame.K_d]:
             self.direction.x = 1
        
        else:
            self.direction.x = 0
            
            
        if key[pygame.K_SPACE]:
            self.ticks += 1
            if self.ticks > 30:
                self.ticks = 0
                Shot("assets/nave/tiro.png", [self.rect.x + 52, self.rect.y - 20], [self.shots])
            
    def limit(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - self.image.get_width():
            self.rect.x = WIDTH - self.image.get_width()
            
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > HEIGHT - self.image.get_height():
            self.rect.y = HEIGHT - self.image.get_height()
            
    
            
            
    def move(self):
        self.rect.center += self.direction * self.speed
        
        
    def update(self):
        self.animation(8, 3, "assets/nave/player")
        self.limit()
        self.input()
        self.move()
        
class Shot(Obj):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self. speed = 5
        
        
    def update(self):
        self.rect.y -= self.speed
        
        
        if self.rect.y < -100:
            self.kill()
            
class Enemy(Obj):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed = 5
        
    def update(self):
        
        self.rect.y += self.speed
        
        if self.rect.y > HEIGHT + self.image.get_height():
            self.kill()
            