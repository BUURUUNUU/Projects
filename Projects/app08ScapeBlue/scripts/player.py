import pygame




class Player(pygame.sprite.Sprite):
    def __init__(self,pos,  groups, colision_group):
        super().__init__(groups)
        
        self.image = pygame.image.load("assets/player/idle_1.png")
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2()
        self.speed = 6
        self.gravity = 0.8
        self.jump_force = 20
        self.colision_group = colision_group
        self.on_ground = False
        
        self.flip = False
        
        self.tick = 0
        self.frame = 0
        
    def input(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_a]:
            self.direction.x = -1
            self.flip = True
            self.animation(8, 3, "assets/player/walk_")
        elif key[pygame.K_d]:
            self.direction.x = 1
            self.flip = False
            self.animation(8, 3, "assets/player/walk_")
        else:
            self.direction.x = 0
            self.animation(8, 2, "assets/player/idle_")
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
        
        
    def x_colision(self):
        for sprite in self.colision_group:
            if sprite.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                    
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
            
        
    def move(self):
        self.rect.x +=self.direction.x * self.speed
        
        if self.on_ground == False:
            self.image = pygame.image.load("assets/player/jump.png")
            self.image = pygame.transform.flip(self.image, self.flip, False)
            
    def gravity_force(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def animation(self, speed, n_img, path):
        self.tick += 1
        if self.tick > speed:
            self.tick = 0
            self.frame = (self.frame + 1) % n_img
            self.image = pygame.image.load(path+ str(self.frame) + ".png")
            self.image = pygame.transform.flip(self.image, self.flip, False)
        
        
            
            
    def update(self):
        self.input()
        self.move()
        self.x_colision()
        self.gravity_force()
        self.y_colision()
            
        