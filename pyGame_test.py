import pygame
#import numpy
import random
#initializing game
pygame.init()

#declaring all the variables
font = pygame.font.SysFont("arial", 48) #font type and size
size = width, height = 800, 600
window = pygame.display.set_mode(size)
running = True #variable set to false to quit game
currentScore = 0
leftEdge = 0 #edges so you don't go off of the screen
rightEdge = 629
bgX = 0 #backround image 1 position
bgX2 = 800 #backround image 2 position
carX = 0 #enemy vehicle postition   
carX2 = 800
rockX = 0
rockX2 = 800
from random import randint
randomNum = randint(0,3)

#loading in images
standingStill = pygame.image.load('images/bikeRight.png')
bgImage = pygame.image.load('images/bgImage.jpg') #1
bgImage2 = pygame.image.load('images/bgImage.jpg') #2
#IMAGES FOR MOTORCYCLE
leftMoveImage = [pygame.image.load('images/bikeLeft.png'),pygame.image.load('images/bikeLeft.png')]
rightMoveImage = [pygame.image.load('images/bikeRight.png'),pygame.image.load('images/bikeRight.png')]
#IMAGES FOR CAR
carLeftMoveImage = [pygame.image.load('images/carLeft.png'),pygame.image.load('images/carLeft.png')]
carRightMoveImage = [pygame.image.load('images/carRight.png'),pygame.image.load('images/carRight.png')]
tankLeftImage = pygame.image.load('images/tankLeft.png')
tankRightImage = pygame.image.load('images/tankRight.png')
camperLeftImage = pygame.image.load('images/camperLeft.png')
rock = pygame.image.load('images/rock.jpeg')
#changing title bar of window
pygame.display.set_caption('Python Final Project')

#setting up the backround music
pygame.mixer.music.load('music/bgmusic.ogg')
pygame.mixer.music.play(-1)

#setting up timer for game fps
timer = pygame.time.Clock()

#class for main motorcycle character
class motorcycle():
    def __init__(self, x, y, width, height): #initialization function for class
        #class attributes
        self.jumping = False
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.still = True
        self.velocity = 10
        self.jumpTime = 8
        self.leftMove = False
        self.rightMove = False
        self.moveCounter = 0
        self.random = 1
        
    def charDraw(self, window): #function to draw character on the screen
        global randomNum
        if randomNum >= 2:
            if not (self.still):
                if self.leftMove == True:
                    window.blit(leftMoveImage[self.moveCounter//35],(self.x,self.y)) #draw left image
                    self.moveCounter += 1
                elif self.rightMove == True:
                    window.blit(rightMoveImage[self.moveCounter//35],(self.x,self.y)) #draw right image
                    self.moveCounter += 1
            else:
                if self.leftMove == True:
                        window.blit(leftMoveImage[0], (self.x,self.y))
                else:
                        window.blit(rightMoveImage[0], (self.x,self.y))
        else:
            if not (self.still):
                if self.leftMove == True:
                    window.blit(carLeftMoveImage[self.moveCounter//35],(self.x,self.y)) #draw left image
                    self.moveCounter += 1
                elif self.rightMove == True:
                    window.blit(carRightMoveImage[self.moveCounter//35],(self.x,self.y)) #draw right image
                    self.moveCounter += 1
            else:
                if self.leftMove == True:
                        window.blit(carLeftMoveImage[0], (self.x,self.y))
                else:
                        window.blit(carRightMoveImage[0], (self.x,self.y))

#class for enemies:
class badGuys():

    def __init__(self, x, y, width, height, stop):
        self.x = x
        self.y = y
        self. width = width
        self.height = height
        self.stop = stop
        self.moveCounter = 0
        self.speed = 4
        self.enemyPath = [self.x, self.stop]

    def drawEnemy(self, window):
        self.moveMe()
        if self.moveCounter + 1 >= 50:
            self.moveCounter = 0

        if self.speed > 0:
            window.blit(tankRightImage, (self.x, self.y)) #drawing tank to the right
            self.moveCounter = self.moveCounter + 1
        else:
            window.blit(tankLeftImage, (self.x, self.y)) #drawing tank to the left
            self.moveCounter = self.moveCounter + 1

    def moveMe(self):
        if self.speed > 0:
            if self.speed + self.x < self.enemyPath[1]: #allowing enemy to move to end
                self.x = self.x + self.speed
            else:
                self.speed = self.speed * -1 #changing directions
                self.moveCounter = 0
        else:
            if self.x - self.speed > self.enemyPath[0]: #checking enemy doesn't pass beginning coordinate
                self.x = self.x + self.speed
            else:
                self.speed = self.speed * -1 #changing directions again (negative * negative equals positive value)
                self.moveCounter = 0
                

#DOESN'T WORK!! class for bullet projectiles DOESN'T WORK!!
class shoot():
    def __init__(self,x,y,color,size,direction):
        self.size = size
        self.color = color
        self.direction = direction
        self.speed = direction * 5
        self.x = x
        self.y = y

    def bulletDraw(self, window):
        pygame.draw.circle(window, self.color, (self.x,self.y), self.size)
        
    
#draw routine
def drawScreen():
    #globalizting needed variables
    global bgX
    global bgX2
    global carX
    global carX2
    global currentScore #globalizing cuerrentScore variable
    global keys
    global rockX
    global rockX2
    #setting up scoreboard
    scoretext = font.render("Score = "+str(currentScore), 1, (0,0,0))
    window.blit(scoretext, (5, 10))
    
    #scrolling backround image
    bgX -= 4
    bgX2 -= 4
    if bgX < -800:
        bgX = 0
        bgX2 = 800
    window.blit(bgImage, (bgX,0)) #drawing the backround image
    window.blit(bgImage2, (bgX2,0)) 
        
    #scrolling vehicles
    carX -= 10
    carX2 -= 10
    if carX < -800:
        carX = 0
        carX2 = 800
    window.blit(camperLeftImage, (carX,540))
    window.blit(camperLeftImage, (carX2,540))

    bike.charDraw(window) #drawin bike
    #tank.drawEnemy(window)

    #if up arrow is pressed draw bullet
    if keys[pygame.K_UP]:
        bullet.bulletDraw(window) #drawing bullet
        bullet.x += 10
        if bullet.x > 500:
            bullet.x = 0
    #blitting score to screen
    window.blit(scoretext, (5, 10))
    pygame.display.update()

    
#initializing object of class 'motorcycle' named 'bike'
bike = motorcycle(0, 501, 171, 99)
#initializing object of class 'badGuys' named 'tank'
tank = badGuys(0, 651, 120, 42, 480)
#initializing bullet object
bullet = shoot(50,550,(0,0,255),5,1)

#game's main loop
while running == True:
    
    #increasing score
    currentScore += 1
    
    timer.tick(45) #game clock setting the fps
    
    for event in pygame.event.get(): #quit when click close in window
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    #moving left and right with arrows keys respectively and standing still
    if keys[pygame.K_LEFT] and bike.x > leftEdge:
        bike.x -= bike.velocity
        bike.leftMove = True
        bike.rightMove = False
        bike.still = False
    elif keys[pygame.K_RIGHT] and bike.x < rightEdge:
        bike.x += bike.velocity
        bike.leftMove = False
        bike.rightMove = True
        bike.still = False
    else:
        bike.moveCounter = 0
        bike.still = True
        
    #jump routine
    if bike.jumping == False: #so you can't double jump
        if keys[pygame.K_SPACE]:
            bike.jumping = True
            bike.rightMove = False
            bike.leftMove = False
            bike.moveCounter = 0
    else:
        if bike.jumpTime >= -8:
            jumpDirection = 1 #postive value to move up
            if bike.jumpTime < 0:
                jumpDirection = -1 #changes direction at top of jump
            bike.y -= (bike.jumpTime ** 2)/2 * jumpDirection #moving y coordinate up or down
            bike.jumpTime -= 1 #decrimenting jump time
        else: #end of jump, reset jump time and jumping bool
            bike.jumping = False 
            bike.jumpTime = 8

    #calling drawScreen function
    drawScreen()
    
pygame.quit()    
