import pygame
pygame.init()

pygame.font.init()

display = pygame.display.set_mode((1024, 640))

campo_img = pygame.image.load("assets/bg.png")
campo = campo_img.get_rect()

player_1_img = pygame.image.load("assets/player_1.png")
player_1 = player_1_img.get_rect()
player_1_speed = 6
player_1_score = 0

player_2_img = pygame.image.load("assets/player_2.png")
player_2 = player_2_img.get_rect(right =1024)
player_2_score = 0

ball_img = pygame.image.load("assets/ball.png")
ball = ball_img.get_rect(center = [1024/2, 640/2])
ball_dir_x = 6
ball_dir_y = 6

font = pygame.font.Font(None, 50)
placar_player_1 = font.render(str(player_1_score), True, "black")
placar_player_2 = font.render(str(player_2_score), True, "black")



cena = "menu"

fps = pygame.time.Clock()

loop = True

while loop:
        
        if cena == "jogo":
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                loop = False

                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_w:
                                        player_1_speed = -6

                                elif event.key == pygame.K_s:
                                        player_1_speed = 6
                                        
                if player_2_score >= 3:
                        cena = "gameover"
                        
                if player_1_score >= 3:
                        cena = "gameover"

                if player_1.y <= 0:
                        player_1.y = 0
                elif player_1.y >= 640 - 150:
                        player_1.y = 640 - 150

                player_1.y += player_1_speed
                
                
                if ball.x <= 0:
                        player_2_score += 1
                        placar_player_2 = font.render(str(player_2_score), True, "black")
                        ball.x = 512
                        ball_dir_x *= -1
                        
                elif ball.x >= 1024:
                        player_1_score += 1
                        placar_player_1 = font.render(str(player_1_score), True, "black")
                        ball.x = 512 
                        ball_dir_x *= -1


                if ball.y <= 0:
                        ball_dir_y *= -1
                elif ball.y >= 640 - 15:
                        ball_dir_y *= -1
                
                ball.x += ball_dir_x
                ball.y += ball_dir_y
                
                player_2.y = ball.y - 75
                
                if player_2.y <= 0:
                        player_2.y = 0
                elif player_2.y >= 640 - 150:
                        player_2.y = 640 - 150
                
                if ball.colliderect(player_1) or ball.colliderect(player_2):
                        ball_dir_x *= -1
                        
                        hit = pygame.mixer.Sound("assets/pong.wav")
                        hit.play()





                display.fill(("white"))
                display.blit(campo_img, campo)
                display.blit(player_1_img, player_1)
                display.blit(player_2_img, player_2)
                display.blit(ball_img, ball)
                
                display.blit(placar_player_1, (300, 50))
                display.blit(placar_player_2, (700, 50))
                
        elif cena == "gameover":
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:   
                                loop = False
                                
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                        cena = "menu"      
                                
                                
                display.fill(("white"))
                text_win = font.render("Game Over", True, "black")
                display.blit(text_win, [400, 320])
                
                
        elif cena == "menu":
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:   
                                loop = False
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                        player_1_score = 0
                                        placar_player_1 = font.render(str(player_1_score), True, "black")
                                        player_2_score = 0
                                        placar_player_2 = font.render(str(player_2_score), True, "black")
                                        player_1.y = 0
                                        player_2.y = 0
                                        
                                        ball.x = 640
                                        ball.y = 350
                                        
                                        cena = "jogo"
                                
                display.fill(("white"))
                title = font.render("Meu jogo", True, "black")
                text = font.render("Press start to play", True, "black")
                display.blit(title, [400, 200])
                display.blit(text, [400, 320])
                
        fps.tick(60)
        pygame.display.update()
        
