import pygame,sys
from pygame import mixer

pygame.init() #Initializing pygame 
screen = pygame.display.set_mode((800,600)) #Creating Screen (width,height)
ball = pygame.image.load('ball.png') #Loading Ball Image
icon = pygame.image.load('pinball.png') #Loading Icon Image For Title Bar
paddle1 = pygame.image.load('paddle1.png') #Loading Paddle Image For Player 1
paddle2 = pygame.image.load('paddle1.png') #Loading Paddle Image For Player 2
mixer.music.load('background.ogg') #Loading Background Music
mixer.music.play(-1) #Playing Background On Loop
pygame.display.set_icon(icon) #Setting Icon On title Bar
pygame.display.set_caption('Pong') #Setting Caption Of Title Bar
# Ball Co-ordinates
ball_x = 0
ball_y = 0
ball_dx = 0.3 #Change In X Coordinate Of Ball
ball_dy = 0.3 #Change In Y Coordinate Of Ball
# Paddle1 Co-ordinates
paddle1_x = 15
paddle1_y = 200
change1 = 0            #This Variable Will Change Y-Coordinate Of Paddle 1
# paddle 2 movements
paddle2_x = 775
paddle2_y = 200
change2 = 0            #This variable Will Change Y-Coordinate Of Paddle 2 

score_value1 = 0       # Storing Score Of Player 1 
score_value2 = 0       # Storing Score Of Player 2
score1 = pygame.font.Font('freesansbold.ttf',100)    # Creating Font to Display On Screen  
score2 = pygame.font.Font('freesansbold.ttf',100)    # Creating Font To Display on Screen
game_over_text = pygame.font.Font('freesansbold.ttf',62)

def draw_ball(x,y):          # Drawing ball On Screen
    screen.blit(ball, (x,y)) 

def draw_paddle1(x,y):
    screen.blit(paddle1, (x,y))

def draw_paddle2(x,y):
    screen.blit(paddle2, (x,y))

def show_text1():
    t = score1.render(str(score_value1),True,(255,0,0))
    screen.blit(t, (200,250))

def show_text2():
    t = score2.render(str(score_value2),True,(0,0,255))
    screen.blit(t, (550,250))

def game_over():
    t = game_over_text.render('GAME OVER!',True,(52, 235, 152))
    screen.blit(t, (235,170))
    
# Main Loop
while True:
    screen.fill((0,0,0)) #Filling Screen With Black Color
    pygame.draw.line(screen,(255,0,0),(0,0),(400,0),10)         #Drawing Border Lines from 59-65
    pygame.draw.line(screen,(255,0,0),(0,0),(0,600),10)
    pygame.draw.line(screen,(255,0,0),(0,600),(400,600),10)
    pygame.draw.line(screen,(0,0,255),(400,0),(800,0),10)
    pygame.draw.line(screen,(0,0,255),(800,0),(800,600),10)
    pygame.draw.line(screen,(0,0,255),(400,600),(800,600),10)
    pygame.draw.line(screen,(255,255,255),(400,0),(400,600),7)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change2 = -0.5
            if event.key == pygame.K_DOWN:
                change2 = 0.5
            if event.key == pygame.K_w:
                change1 = -0.5
            if event.key == pygame.K_s:
                change1 = 0.5

            if event.key == pygame.K_RETURN:
                score_value1=0
                score_value2=0
                ball_dx = 0.3
                ball_dy = 0.3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                change2 = 0
            if event.key == pygame.K_DOWN:
                change2 = 0
            if event.key == pygame.K_w:
                change1 = 0
            if event.key == pygame.K_s:
                change1 = 0

    if paddle1_y <= 0:
        paddle1_y = 0
    
    if paddle1_y >= 459:
        paddle1_y = 459 
    
    if paddle2_y <= 0:
        paddle2_y = 0
    
    if paddle2_y >= 459:
        paddle2_y = 459

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_y >= 584:
        ball_y = 584
        ball_dy = -0.3
    
    if ball_y <= 0:
        ball_y = 0
        ball_dy = 0.3

    if (ball_x<=14) and (int(ball_y) in list(range(int(paddle1_y), int(paddle1_y+141)))):
        s = mixer.Sound('pong.ogg')
        mixer.Sound.play(s)
        ball_dx = 0.3
    
    if (ball_x>=760) and (int(ball_y) in list(range(int(paddle2_y), int(paddle2_y+141)))):
        e = mixer.Sound('pong.ogg')
        mixer.Sound.play(e)
        ball_dx = -0.3


    if ball_x<=-17:
        score_value2+=1 
        pygame.time.delay(1000)
        ball_x=400
        ball_y=300

    if ball_x>=801:
        score_value1+=1
        pygame.time.delay(1000)
        ball_x=400
        ball_y=300
    
    if score_value2 >= 10 or score_value1 >= 10:
        game_over()
        ball_dx = 0
        ball_dy = 0
    
    paddle1_y += change1
    paddle2_y += change2
    draw_ball(ball_x,ball_y)
    draw_paddle1(paddle1_x,paddle1_y)
    draw_paddle2(paddle2_x,paddle2_y)
    show_text1()
    show_text2()
    pygame.display.update() #Updating The Display
