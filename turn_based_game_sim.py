import pygame
from char_class_info import Conjurer
from char_class_info import Medeian

pygame.init()

class GameSIM:

    #initialize screen
    screen = pygame.display.set_mode((800,600))

    #create two characters
    character_1 = Conjurer()
    character_2 = Medeian()

    #initialize player 1
    init_character = character_1


    #first test at gameplay loop
    fighting = True
    while fighting:
        for event in pygame.event.get():
            if event.type() == pygame.QUIT:
                fighting = False

        
        #clear the screen

        #draw a sprite of the character

        #update display

        #create key bindings

        #get a target character for player 1

        #game loop for turn based attack

        #check if game is over


    pygame.quit()

