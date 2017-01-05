import pygame
import time
import random

white = (255,255,255)
black=(0,0,0)
red = (255,0,0)
dGreen =(0,155,0)
green = (0,255,0)
display_width =800
display_height = 600
clock = pygame.time.Clock()
FPS =20
block_size = 10
pygame.init()

icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)     # 32*32 is best

gameDisplay = pygame.display.set_mode ((display_width,display_height))
pygame.display.set_caption('Slither')


img = pygame.image.load('snakeHead.png')
direction = 'right'
appleimg = pygame.image.load('apple.png')

def Pause():
    pause =True

    while pause:
        gameDisplay.fill(white)
        message_to_user('Paused', y_displace=-100, fontSize=60, color=dGreen)
        message_to_user('Press C to play, P to pause and Q to Quit', color=black, fontSize=25, y_displace=40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pause = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(5)

def score(score):
    font = pygame.font.SysFont("monospace", 20)
    text= font.render( 'Score: '+str(score), True, black)
    gameDisplay.blit(text, [0,0])


def randAppleGen():
    randAppleX = random.randrange(0,(display_width-block_size)/block_size)*block_size
    randAppleY = random.randrange(0, (display_height - block_size) / block_size) * block_size
    return randAppleX,randAppleY




def IntroLoop():

    introLoop = True

    while introLoop:
        gameDisplay.fill(white)
        message_to_user('Welcome to Slither', y_displace=-100, fontSize=60,color=dGreen)
        message_to_user('This is the best snake game you will ever play', y_displace=-50, color=black,fontSize=20)
        message_to_user('Press C to play, P to pause and Q to Quit', color=dGreen, fontSize=25, y_displace=40)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    introLoop = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
    clock.tick(5)


def snake( block_size, snakeList):


    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(img, 90)
    if direction == 'up':
        head = pygame.transform.rotate(img, 0)
    if direction == 'down':
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakeList[-1][0],snakeList[-1][1]))

    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])


def message_to_user(msg, color,y_displace = 0,fontSize = 25):
    font = pygame.font.SysFont("monospace", fontSize)
    textSurf = font.render(msg,True, color)
    textRect= textSurf.get_rect()
    textRect.center = [display_width/2,display_height/2 + y_displace]
    gameDisplay.blit(textSurf,textRect)

def GameLoop():
    global direction
    leadX = display_width / 2
    leadY = display_height / 2
    lead_x_change = block_size
    lead_y_change = 0
    gameExit = False
    gameOver = False

    randAppleX, randAppleY = randAppleGen()


    snakeList = []
    snakeLength = 1

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_user('GAME OVER',red,fontSize= 80)
            message_to_user('press C to play again, Q to exit',red,y_displace= 100, fontSize= 30)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                    if event.key == pygame.K_c:
                        GameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change= -block_size
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change= block_size
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change= -block_size
                    lead_x_change = 0
                if event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change= block_size
                    lead_x_change = 0
                if event.key == pygame.K_p:
                    Pause()

        if leadX < 0 or leadX >= display_width or leadY <0 or leadY>=display_height:
            gameOver= True

        leadX += lead_x_change
        leadY += lead_y_change
        gameDisplay.fill(white)
        gameDisplay.blit(appleimg,[randAppleX,randAppleY])
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size,block_size])

        snakeHead=[leadX,leadY]
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        for seg in snakeList[:-1]:
            if seg == snakeHead:
                gameOver = True



        snake(block_size,snakeList)
        score(snakeLength - 1)

        pygame.display.update()  # Finally after all is done

        if leadX== randAppleX and leadY == randAppleY:
            snakeLength +=1
            randAppleX, randAppleY = randAppleGen()


        clock.tick(FPS)


    gameDisplay.fill(white)
#    message_to_user('You lose, Suckaaa!!!',red)
    pygame.display.update()
#    time.sleep(1)
    pygame.quit()
    quit()



IntroLoop()
GameLoop()