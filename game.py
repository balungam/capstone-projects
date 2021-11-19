#This was one of the most challenging tasks yet.

#This task is all about creating a simple game using pygame.
#the first thing you need is to make sure you have pygame installed on your system.
#when you start writing this program you first have to "import pygame"and "import random" 
import pygame
import random
#We have to initialize the pygame befeore we can start.
pygame.init()

#We need to create a surface for a game. 
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))

#We have given the game a title "moving_pictures "
pygame.display.set_caption('moving_pictures')

#We set the back ground to RED
background_color = (255,0,0)

#We loaded 5 images one player, three enemies and one prize.
player = pygame.image.load("bay1.jpg")
enemy = pygame.image.load("vader.jpg")
enemy2 = pygame.image.load("yoda.jpg")
enemy3 = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")

#Some of the image sizes were big for the surface we created, so we had to create a default image size. 
DEFAULT_IMAGE_SIZE = (100,100)

DEFAULT_IMAGE_SIZE2 = (80,80)
#we transformed the images to a uniform image size.
player = pygame.transform.scale(player,DEFAULT_IMAGE_SIZE)
enemy = pygame.transform.scale(enemy,DEFAULT_IMAGE_SIZE2)
enemy2 = pygame.transform.scale(enemy2,DEFAULT_IMAGE_SIZE2)
enemy3 = pygame.transform.scale(enemy3,DEFAULT_IMAGE_SIZE2)
prize = pygame.transform.scale(prize,DEFAULT_IMAGE_SIZE2)
#we had to get/set the image height and width
image_height = player.get_height()
image_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))
#we had to set the player's position.
playerXPosition = 500
playerYPosition = 50
#We also had to set the enemies position.With a random height each time the game lops through.
enemyXPosition = screen_width
enemyYPosition = random.randint(0,screen_height - enemy_height)

enemy2XPosition = screen_width
enemy2YPosition = random.randint(0,screen_height - enemy2_height)

enemy3XPosition = screen_width
enemy3YPosition = random.randint(0,screen_height - enemy3_height)

prizeXPosition = screen_width
prizeYPosition = random.randint(0,screen_height - prize_height)
#We will also use the arrow keys to move the player. 
keyUp= False
keyDown= False
keyLeft= False

#we formed a while loop to execute all functions of the game especially the movements of the player.

while 1:
    #the screen.fill controls the color of the surface, we used the variable background_color
    screen.fill(background_color)
    #screen.blit means we will be able to move an object from one block to another.
    screen.blit(player,(playerXPosition, playerYPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    #the "display.flip" will refresh the surface after each and every loop.
    pygame.display.flip()
#the for loop will is mainly for confirming when a key is pressed or not and what action needs to be taken.
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        playerXPosition -= 2

    if keys_pressed[pygame.K_RIGHT]:
        playerXPosition += 2

    if keys_pressed[pygame.K_UP]:
        playerYPosition -= 2

    if keys_pressed[pygame.K_DOWN]:
        playerYPosition += 2
         

#The playerbox, enemy and prize boxes will help us with detecting a collision between the 5.     

    playerBox = pygame.Rect(player.get_rect())


    playerBox.top = playerYPosition
    playerBox.left = playerXPosition


    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.right = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.right = enemy3XPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.right = prizeXPosition

#if the player collides with any one of the three enemies the game is over and the player loses.
    if playerBox.colliderect(enemyBox):
        print("You lose!")
        pygame.quit()
        exit(0)
        
    if playerBox.colliderect(enemy2Box):
        print("You lose!")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):
        print("You lose!")
        pygame.quit()
        exit(0)
#if the enemy doesn't collide with the player the enemy will come right back again.

    if enemyXPosition < 0 - enemy_width:
             
        enemyXPosition = screen_width
        enemyYPosition = random.randint(0,screen_height - enemy_height)
       
    enemyXPosition -= 0.20

    if enemy2XPosition < 0 - enemy2_width:

        enemy2XPosition = screen_width
        enemy2YPosition = random.randint(0,screen_width - enemy2_width)
    
    enemy2XPosition -= 0.20

    if enemy3XPosition < 0 - enemy3_width:

        enemy3XPosition = screen_width
        enemy3YPosition = random.randint(0,screen_height - enemy3_height)

    enemy3XPosition -= 0.20
#if the player colides with the prize the player wins the game otherwise the prize will come right back again.      
    if prizeXPosition < 0 - prize_width:

        prizeXPosition = screen_width
        prizeYPosition = random.randint(0,screen_height - prize_height)

    if playerBox.colliderect(prizeBox):
        print("You win!!!")
        pygame.quit()
        exit(0)
    
    prizeXPosition -= 0.10

#reference: images "vader" and "yoda" were downloaded from the internet.
