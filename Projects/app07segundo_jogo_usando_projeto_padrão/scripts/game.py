import pygame
from scripts.scene import Scene
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.settings import *
import random
from scripts.text import Text

class Game(Scene):

    def __init__(self):
        super().__init__()

        self.bg = AnimatedBg("assets/menu/bg.png", [0 ,0], [0, -640], [self.all_sprites]) 
        self.spaceship =  SpaceShip("assets/nave/player0.png", [450, 500], [self.all_sprites])
        
        self.pts = 0
        self.score_text = Text("assets/fonts/font_1.ttf", 25, "Score ", "white", [30, 30])
        self.score_pts = Text("assets/fonts/font_1.ttf", 25, "0", "white", [150, 30])
        
        self.life1 = Obj("assets/nave/vida.png", [30, 60], [self.all_sprites])
        self.life2 = Obj("assets/nave/vida.png", [70, 60], [self.all_sprites])
        self.life3 = Obj("assets/nave/vida.png", [110, 60], [self.all_sprites])
        
        
        self.tick = 0   
        
        self.enemy_colision = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        
    def hud(self):
        if self.spaceship.life == 2:
            self.life3.kill()
        elif self.spaceship.life ==1:
            self.life2.kill()
        elif self.spaceship.life == 0:
            self.life1.kill()
        
        
        
        
        
        
        
    def spawn_enemy(self):
        self.tick += 1
        if self.tick == 60:

            BigShip("assets/nave/enemy3_0.png", [random. randint(100, 1180), -100], [self.all_sprites, self.enemy_colision])
        elif self.tick ==180:
            
            MediumShip("assets/nave/enemy2_0.png", [random. randint(100, 1180), -100], [self.all_sprites, self.enemy_colision])
            MediumShip("assets/nave/enemy2_0.png", [random. randint(100, 1180), -100], [self.all_sprites, self.enemy_colision])
        elif self.tick ==270:
            
            SmallShip("assets/nave/enemy0.png", [random. randint(100, 1180), -100], [self.all_sprites, self.enemy_colision])
            SmallShip("assets/nave/enemy0.png", [random. randint(100, 1180), -100], [self.all_sprites, self.enemy_colision])
            SmallShip("assets/nave/enemy0.png", [random. randint(100, 1180), -100], [self.all_sprites, self.enemy_colision])
            SmallShip("assets/nave/enemy0.png", [random. randint(100, 1180), -100], [self.all_sprites, self.enemy_colision])
            
            PowerUp("assets/nave/powerup0.png",[random. randint(100, 1180), -100], [self.all_sprites, self.powerups])
            
            self.tick = 0
            
            
    def colision(self):
        for shot in self.spaceship.shots:
            for enemy in self.enemy_colision:
                if shot.rect.colliderect(enemy.rect):
                    shot.kill()
                    enemy.life -= 1
                    self.pts += 1
                    self.score_pts.update_text(str(self.pts))
                    
        for enemy in self.enemy_colision:
            if self.spaceship.rect.colliderect(enemy.rect):
                enemy.kill()         
                self.spaceship.life -= 1   
                self.spaceship.level = 1
                print(self.spaceship.life)
                
        for powerup in self.powerups:
            if self.spaceship.rect.colliderect(powerup.rect):
                powerup.kill()
                self.spaceship.level += 1

    def gameover(self):
        if self.spaceship.life <= 0:
            self.active = False
        
    def update(self):
        self.colision()
        self.spaceship.shots.draw(self.display)
        self.spaceship.shots.update()
        self.bg.update()
        self.spaceship.input()
        self.spawn_enemy()
        self.score_text.draw()
        self.score_pts.draw()
        self.gameover()
        self.hud()
        return super().update()
    
    
class SpaceShip(Obj):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.level = 1
        
        self.life = 3
        
        
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
                if self.level == 1:
                    Shot("assets/nave/tiro1.png", [self.rect.x + 52, self.rect.y - 20], [self.shots])
                elif self.level == 2:
                    Shot("assets/nave/tiro2.png", [self.rect.x + 52, self.rect.y - 20], [self.shots])
                elif self.level == 3:
                    Shot("assets/nave/tiro3.png", [self.rect.x + 52, self.rect.y - 20], [self.shots])
                elif self.level == 4:
                    Shot("assets/nave/tiro1.png", [self.rect.x, self.rect.y - 20], [self.shots])
                    Shot("assets/nave/tiro1.png", [self.rect.x + 100, self.rect.y - 20], [self.shots])
                elif self.level == 5:
                    Shot("assets/nave/tiro2.png", [self.rect.x, self.rect.y - 20], [self.shots])
                    Shot("assets/nave/tiro2.png", [self.rect.x + 100, self.rect.y - 20], [self.shots])
                elif self.level == 6:
                    Shot("assets/nave/tiro3.png", [self.rect.x, self.rect.y - 20], [self.shots])
                    Shot("assets/nave/tiro3.png", [self.rect.x + 100, self.rect.y - 20], [self.shots])
                else:
                    Shot("assets/nave/tiro3.png", [self.rect.x, self.rect.y - 20], [self.shots])
                    Shot("assets/nave/tiro3.png", [self.rect.x + 10, self.rect.y - 20], [self.shots])
                    Shot("assets/nave/tiro3.png", [self.rect.x + 20, self.rect.y - 20], [self.shots])
                    Shot("assets/nave/tiro3.png", [self.rect.x + 50, self.rect.y - 20], [self.shots])
            
            
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
        
        self.speed = 1
        self.life = 1
        
        
    def destruction(self):
        if self.life <= 0:
            self.kill()
            
    def limits(self):
        self.limits()
        if self.rect.y > HEIGHT + self.image.get_height():
            self.kill()
            
            
    def move(self):
          self.rect.y += self.speed
        
    def update(self):
        self.move()
        self.destruction()
        
        
class SmallShip(Enemy):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed = 6
        self.life = 1
        
    def update(self):
        self.animation(8, 3, "assets/nave/enemy")
        return super().update()
      
      
class MediumShip(Enemy):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed = 4
        self.life= 2
            
    def update(self):
        self.animation(8, 1, "assets/nave/enemy2_")
        return super().update()
    
    
class BigShip(Enemy):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed =1
        self.life = 10
        
    def update(self):
        self.animation(16, 1, "assets/nave/enemy3_")
        
        return super().update()
    
    
class PowerUp(Enemy):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed = 2
        
    def update(self):
        self.animation(16, 3, "assets/nave/powerup")
        return super().update()