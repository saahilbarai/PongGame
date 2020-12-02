import pygame,sys,random

##initialize pygame
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Saahil's game")

#game graphics 
middle_rectangle1 = pygame.Rect(screen_width/2, 0,10,screen_height/2 -100)
middle_rectangle2 = pygame.Rect(screen_width/2, screen_height/2 +100,10,screen_height/2 -100)
paddle_color = (255, 64, 129)
background_color = (255,255,255)
ball_color = (63, 81, 181)

#game rectangles
ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10,20,20)
graphiccircle = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10,200,200)
player = pygame.Rect(screen_width -20, screen_height/2 -70, 10,140)
opponent = pygame.Rect(10, screen_height/2 -70, 10,140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)
cool_grey = (94,110,133)


ballspeedx = 7
ballspeedy = 7
playerspeed = 0
opponentspeed = 7

playerscore = 0
opponenetscore = 0

pongsound = pygame.mixer.Sound("pop1.wav")


scoretimer = True



scorefont = pygame.font.Font("freesansbold.ttf",20)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerspeed +=7
            if event.key == pygame.K_UP:
                playerspeed -=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerspeed -=7
            if event.key == pygame.K_UP:
                playerspeed +=7
        
    
    
    ball.x+= ballspeedx
    ball.y+= ballspeedy
    
    if ball.top <= 0 or ball.bottom >= screen_height:
        ballspeedy *= -1
    if ball.left <= 0:
        #ball.center = (screen_width/2,screen_height/2)
        #ballspeedy *= random.choice((-1,1))
        #ballspeedx *= random.choice((-1,1))
        playerscore += 1
        scoretimer = pygame.time.get_ticks()
        
    if ball.right >= screen_width:
        #ball.center = (screen_width/2,screen_height/2)
        #ballspeedy *= random.choice((-1,1))
        #ballspeedx *= random.choice((-1,1))
        opponenetscore += 1
        scoretimer = pygame.time.get_ticks()
        
    if ball.colliderect(player) and ballspeedx > 0:
        pygame.mixer.Sound.play(pongsound)
        if(ball.right - player.left) < 10:
            ballspeedx *= -1
        elif(ball.bottom - player.top) < 10 and ballspeedy > 10:
            ballspeedy *= -1
        elif(ball.top - player.bottom) < 10 and ballspeedy < 0:
            ballspeedy *= -1
    
    if ball.colliderect(opponent) and ballspeedx < 0:
        pygame.mixer.Sound.play(pongsound)
        if(ball.left - opponent.right < 10):
            ballspeedx *= -1
        elif(ball.bottom - opponent.top) < 10 and ballspeedy > 10:
            ballspeedy *= -1
        elif(ball.top - opponent.bottom) < 10 and ballspeedy < 0:
            ballspeedy *= -1
        
    player.y += playerspeed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    
    if opponent.top < ball.y:
        opponent.top += opponentspeed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponentspeed
    
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,middle_rectangle1)
    pygame.draw.rect(screen,light_grey,middle_rectangle2)
    pygame.draw.rect(screen,paddle_color, player)
    pygame.draw.rect(screen,paddle_color, opponent)
    pygame.draw.ellipse(screen, ball_color,ball)
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height/2 - 100))
    pygame.draw.aaline(screen,light_grey,(screen_width/2,screen_height),(screen_width/2,screen_height/2 +100))
    pygame.draw.circle(screen,light_grey,(400 , 300),105,10)
    

    
    if scoretimer:
        current_time = pygame.time.get_ticks()
        ball.center = (screen_width/2,screen_height/2)
        
        if(current_time - scoretimer < 1000):
            number_three = scorefont.render("3",False,light_grey)
            screen.blit(number_three,(screen_width/2-5,screen_height/2 +40))
        if(1000 < current_time - scoretimer < 2000):
            number_two = scorefont.render("2",False,light_grey)
            screen.blit(number_two,(screen_width/2-5,screen_height/2 +40))
        if(2000 < current_time - scoretimer < 3000):
            number_one = scorefont.render("1",False,light_grey)
            screen.blit(number_one,(screen_width/2-5,screen_height/2 +40))
        
        
        if(current_time - scoretimer < 3000):
            ballspeedx = 0
            ballspeedy = 0
        else:
            ballspeedy = 7 * random.choice((-1,1))
            ballspeedx = 7 * random.choice((-1,1))
            scoretimer = None
        
    playertext = scorefont.render(f"{playerscore}",False,light_grey)
    screen.blit(playertext,(420,290))
    opponenttext = scorefont.render(f"{opponenetscore}",False,light_grey)
    screen.blit(opponenttext,(372,290))
    
    pygame.display.flip()
    clock.tick(60)

    
    
            
            