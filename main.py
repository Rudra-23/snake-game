import pygame
import random
from sys import exit
pygame.init()

screen_width=900
screen_height=500

gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("MYGame")

clock=pygame.time.Clock()
fps=30
def plotsnake(gameWindow,color,snake_l,snake_size):
    for x,y in snake_l:
        pygame.draw.rect(gameWindow,color,(x,y,snake_size,snake_size))
font =pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    stext=font.render(text,True,color)
    gameWindow.blit(stext,[x,y])

def gameloop():
    score=0
    snake_l=[]
    white =(255,255,255)
    red =(255,0,0)
    black=(0,0,0)
    snake_x=50
    snake_y=60
    snake_size=30
    velocity_x=0
    velocity_y=0
    game_over=False
    game_exit=False
    food_x=random.randint(40,screen_width-20)
    food_y=random.randint(40,screen_height-20)
    length=1
    while not game_exit:
        if game_over:
            gameWindow.fill(black)
            text_screen("GAME OVER - TRY AGAIN",white,200,200)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    gameloop()
                if event.type == pygame.QUIT:
                    game_exit=True
            

        else:       
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit=True
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s or event.key ==pygame.K_DOWN:
                        velocity_y=10
                        velocity_x=0
                    if event.key == pygame.K_w or event.key ==pygame.K_UP:
                        velocity_y=-10
                        velocity_x=0
                    if event.key == pygame.K_d or event.key ==pygame.K_RIGHT:
                        velocity_y=0
                        velocity_x=10
                    if event.key == pygame.K_a or event.key ==pygame.K_LEFT:
                        velocity_y=0
                        velocity_x=-10
            snake_x += velocity_x
            snake_y += velocity_y
            
            if abs(food_x-snake_x)<20 and abs(food_y-snake_y)<20:
                food_x =random.randint(40,screen_width-20)
                food_y =random.randint(40,screen_height-20)
                length +=5
                score +=1

            gameWindow.fill(white)
            text_screen("SCORE : "+str(score),red,5,5)
            pygame.draw.rect(gameWindow,red,(food_x,food_y,snake_size,snake_size))

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_l.append(head)
            if len(snake_l)>length:
                del snake_l[0]
            if head in snake_l[:-1]:
                game_over=True

            if snake_x<0 or snake_y<0 or snake_x>screen_width or snake_y>screen_height:
                game_over=True

            plotsnake(gameWindow,black,snake_l,snake_size)

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    exit()
            

gameloop()
