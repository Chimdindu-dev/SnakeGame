import pygame
import time
import random

#start game
pygame.init()
#board
ScreenWidth = 500
ScreenHeight = 500
Screen = pygame.display.set_mode((500,500))

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    Screen.blit(mesg, [ScreenWidth/2, ScreenHeight/2])

#screen changes
pygame.display.update()
pygame.display.set_caption('Snake game for MLH')
font_style = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
PastelPink = (255,209,220)


def gameLoop():
    game_over = False
    game_close = False

    x1 = 250
    y1 = 250

    x1_change = 0       
    y1_change = 0

    snakeblock = 20
    foodx = round(random.randrange(0, ScreenWidth - snakeblock) / 10.0) * 10.0
    foody = round(random.randrange(0, ScreenWidth - snakeblock) / 10.0)

    while not game_over:
        while game_close == True:
            Screen.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    gameLoop()


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True #press x to close game
            #print(event)   #prints out all the actions that take place on the screen
            #pygame.draw.rect(Screen,blue,[250,250,20,20])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0

            if x1 >= ScreenWidth or x1 < 0 or y1 >= ScreenHeight or y1 < 0:
                game_over = True

        x1 += x1_change
        y1 += y1_change
        Screen.fill(white)
        pygame.draw.ellipse(Screen,PastelPink,[x1,y1,20,20])
        pygame.draw.rect(Screen, blue, [foodx, foody, snakeblock, snakeblock])
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            print("Yummy!!")

        clock.tick(10) #snake speed 

message("You lost",black)
pygame.display.update()
#time.sleep(2)

#stop game
pygame.quit()
quit()

