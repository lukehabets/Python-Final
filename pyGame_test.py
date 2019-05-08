import pygame

#initializing game
pygame.init()

#declaring all the variables
font = pygame.font.SysFont("arial", 48)
size = width, height = 800, 600
window = pygame.display.set_mode(size)
run = True
width = 171 #width of sprite
height = 99 #height of sprite
velocity = 10
currentScore = 0
x = 0
y = 501
leftEdge = 0
rightEdge = 629
jumping = False
jumpTime = 8
leftMove = False
rightMove = False
moveCounter = 0

class player(object):
    def _init_self(self, x, y, width, height):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        
#loading in images
standingStill = pygame.image.load('images/bikeRight.png') #bike just sits facing right when not moving
bgImage = pygame.image.load('images/bgImage.jpg')
leftMoveImage = [pygame.image.load('images/bikeLeft.png'),pygame.image.load('images/bikeLeft.png')]
rightMoveImage = [pygame.image.load('images/bikeRight.png'),pygame.image.load('images/bikeRight.png')]

#setting up timer for game fps
timer = pygame.time.Clock()

#draw routine
def drawScreen():
    global currentScore
    global moveCounter
    #setting up scoreboard
    scoretext = font.render("Score = "+str(currentScore), 1, (0,0,0))
    window.blit(scoretext, (5, 10))
   
    window.blit(bgImage, (0,0))
    if leftMove == True:
        window.blit(leftMoveImage[moveCounter//35],(x,y))
        moveCounter += 1
    elif rightMove == True:
        window.blit(rightMoveImage[moveCounter//35],(x,y))
        moveCounter += 1
    else:
        window.blit(standingStill, (x,y))
    #blitting score to screen
    window.blit(scoretext, (5, 10))
    pygame.display.update()
    
#changing title bar of window
pygame.display.set_caption('Python Final Project')

#setting up the backround music
pygame.mixer.music.load('music/bgmusic.ogg')
pygame.mixer.music.play(-1)

while run == True:
    #increasing score
    currentScore += 1
    
    timer.tick(45) #game clock setting the fps
    
    for event in pygame.event.get(): #quit when click close in window
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() #assigning var named 'keys' to keypress

    #moving left and right with arrows respectively
    if keys[pygame.K_LEFT] and x > leftEdge:
        x -= velocity
        leftMove = True
        rightMove = False
    elif keys[pygame.K_RIGHT] and x < rightEdge:
        x += velocity
        leftMove = False
        rightMove = True
    else:
        moveCounter = 0
        rightMove = False
        leftMove = False
        
    #jump routine
    if jumping == False: #so you can't double jump
        if keys[pygame.K_SPACE]:
            jumping = True
            rightMove = False
            leftMove = False
            moveCounter = 0
    else:
        if jumpTime >= -8:
            jumpDirection = 1 #postive value to move up
            if jumpTime < 0:
                jumpDirection = -1 #changes direction at top of jump
            y -= (jumpTime ** 2)/2 * jumpDirection #moving y coordinate up or down
            jumpTime -= 1 #decrimenting jump time
        else: #end of jump, reset jump time and jumping bool
            jumping = False 
            jumpTime = 8

    #calling drawScreen function
    drawScreen()
    
pygame.quit()    
