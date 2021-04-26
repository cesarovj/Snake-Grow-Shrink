#Imports the libraries
import pygame
import random

#Initializes pygame
pygame.init()

#Creates game widnow with a title
width = 600
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake: Grow or Shrink')

#Color of snake
tailColor = (107, 142, 35)
outerColor = (128, 128, 0)
innerColor = (154, 205, 50)

#Color of the differe foods
foodColor = (105,105,105)
poisonColor = (220, 20, 60)

#Color of background
bgColor = (189, 183, 107)

#Color of text and end window
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

#Creat a clock so game continues to run
clock = pygame.time.Clock()

#Features of snake
cellSize = 10
snakeSpeed = 13

#Creates fonts
messageFont = pygame.font.SysFont(None, 40)
scoreFont = pygame.font.SysFont(None, 25)

#Creates the Scoreboard
def drawScore(score):
    text = scoreFont.render('Score: ' + str(score), True, white)
    window.blit(text, [0,0])

#Creates the snake
def drawSnake(cellSize, cellPixels):
    head = 1
    for cell in cellPixels:
        #Draws rectangles on the window and gives it x and y cordinates in comparison with width and height
        if head == 0:
            pygame.draw.rect(window, outerColor, [cell[0], cell[1], cellSize, cellSize])
            pygame.draw.rect(window, innerColor, [cell[0] + 1, cell[1] + 1, cellSize - 2, cellSize -2])
        if head == 1:
            pygame.draw.rect(window, outerColor, [cell[0], cell[1], cellSize, cellSize])
            pygame.draw.rect(window, tailColor, [cell[0] + 1, cell[1] + 1, cellSize - 2, cellSize -2])
            head = 0

#Creates the game
def runGame():
    gameOver = False
    gameClose = False

    #Starting position for the snake
    snakePosx = width / 2
    snakePosy = height / 2

    #Snake is not moving until user makes it move in the begining
    xSpeed = 0
    ySpeed = 0

    #Empty list, which overtime the snake will grow or shrink causing to add or remove in the list
    cellPixels = []
    #Starting size of snake
    snakeSize = 1

    #Random postion for the different foods
    foodX = round(random.randrange(0, width - cellSize) / 10.0) * 10
    foodY = round(random.randrange(0, height - cellSize) / 10.0) * 10
    poisonX = round(random.randrange(0, width - cellSize) / 10.0) * 10
    poisonY = round(random.randrange(0, height - cellSize) / 10.0) * 10

    foodX2 = round(random.randrange(0, width - cellSize) / 10.0) * 10
    foodY2 = round(random.randrange(0, height - cellSize) / 10.0) * 10
    poisonX2 = round(random.randrange(0, width - cellSize) / 10.0) * 10
    poisonY2 = round(random.randrange(0, height - cellSize) / 10.0) * 10

    #While the game is not done, keep iterating
    while not gameOver:
        
        #The game might be game over but you can decide if want to close or play again
        while gameClose:
            window.fill(black)
            gameOverTxt = messageFont.render('Game Over!', True, red)
            window.blit(gameOverTxt, [width / 3, height / 3])
            messageTxt = scoreFont.render('Press Return To Play Again or Press Spacebar To Exit', True, red)
            window.blit(messageTxt, [width // 2 - 225, height // 2 + 10])
            drawScore(snakeSize - 1)
            pygame.display.update()

            #Key bindings for playing again or closing the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_RETURN:
                        runGame()
                if event.type == pygame.QUIT:
                    gameOver = True
                    gameClose = False

        #Loop for event
        for event in pygame.event.get():
            #Quit event
            if event.type == pygame.QUIT:
                gameOver = True
            #Movement events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xSpeed = -cellSize
                    ySpeed = 0
                if event.key == pygame.K_RIGHT:
                    xSpeed = cellSize
                    ySpeed = 0
                if event.key == pygame.K_UP:
                    xSpeed = 0
                    ySpeed = -cellSize
                if event.key == pygame.K_DOWN:
                    xSpeed = 0
                    ySpeed = cellSize

        #If the snake collides to the walls the game will end
        if snakePosx >+ width or snakePosx < 0 or snakePosy >= height or snakePosy < 0:
            gameClose = True
        
        #Movement based on speed
        snakePosx += xSpeed
        snakePosy += ySpeed

        #Draws the window and different foods
        window.fill(bgColor)
        pygame.draw.rect(window, foodColor, [foodX, foodY, cellSize, cellSize])
        pygame.draw.rect(window, poisonColor, [poisonX, poisonY, cellSize, cellSize])
        pygame.draw.rect(window, foodColor, [foodX2, foodY2, cellSize, cellSize])
        pygame.draw.rect(window, poisonColor, [poisonX2, poisonY2, cellSize, cellSize])

        cellPixels.append([snakePosx, snakePosy])
        
        if len(cellPixels) > snakeSize:
            del cellPixels[0]
        
        #Checking if the snake runs into itself
        for cell in cellPixels[:-1]:
            if cell == [snakePosx, snakePosy]:
                gameClose = True

        drawSnake(cellSize, cellPixels)
        drawScore(snakeSize - 1)

        #Updates the display each time an event occurs
        pygame.display.update()

        #randomizes the different foods once eaten and score changes depending on the food eaten
        if (snakePosx == foodX and snakePosy == foodY) or (snakePosx == foodX2 and snakePosy == foodY2):
            foodX = round(random.randrange(0, width - cellSize) / 10) * 10
            foodY = round(random.randrange(0, height - cellSize) / 10) * 10
            poisonX = round(random.randrange(0, width - cellSize) / 10) * 10 
            poisonY = round(random.randrange(0, height - cellSize) / 10) * 10
            foodX2 = round(random.randrange(0, width - cellSize) / 10) * 10
            foodY2 = round(random.randrange(0, height - cellSize) / 10) * 10
            poisonX2 = round(random.randrange(0, width - cellSize) / 10) * 10
            poisonY2 = round(random.randrange(0, height - cellSize) / 10) * 10
            snakeSize += 1
                
        if (snakePosx == poisonX and snakePosy == poisonY) or (snakePosx == poisonX2 and snakePosy == poisonY2):
            poisonX = round(random.randrange(0, width - cellSize) / 10) * 10
            poisonY = round(random.randrange(0, height - cellSize) / 10) * 10
            foodX = round(random.randrange(0, width - cellSize) / 10) * 10
            foodY = round(random.randrange(0, height - cellSize) / 10) * 10
            poisonX2 = round(random.randrange(0, width - cellSize) / 10) * 10 
            poisonY2 = round(random.randrange(0, height - cellSize) / 10) * 10
            foodX2 = round(random.randrange(0, width - cellSize) / 10) * 10
            foodY2 = round(random.randrange(0, height - cellSize) / 10) * 10
            snakeSize -= 1
            cellPixels.remove([snakePosx, snakePosy])
            if snakeSize < 1:
                gameClose = True
        
        clock.tick(snakeSpeed)

    pygame.quit()
    quit()

runGame()
