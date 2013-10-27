#------------------------------------------------------------------------
# Library Imports
#------------------------------------------------------------------------

import pygame, sys, os
from pygame.sprite import Sprite
from random import randint, choice
from pygame.locals import *
from time import gmtime

NUMBER_OF_DOZES = 10

def time_blocker():
    pass
    #while ((gmtime().tm_hour == 16 and gmtime().tm_min == 41 and gmtime().tm_sec == 59) == False) and ((gmtime().tm_hour == 16 and gmtime().tm_min == 42 and gmtime().tm_sec == 59) == False):
      #  print gmtime()
       # pygame.time.wait(1000)
    #pygame.time.wait(1000)
    
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
    return sound
    
def deadline(screen, completed_dozes):
    pygame.mixer.music.load("alarm1.mp3")
    pygame.mixer.music.play(-1)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == KEYDOWN:
                pygame.mixer.music.stop()
                completed_dozes += 1
                if completed_dozes == NUMBER_OF_DOZES:
                    completed_dozes = 0
                    screen.fill(Color('black'))
                    rect = Rect(100,100, 10, 10)            
                    msg = 'No dozes for now'
                    my_font = pygame.font.SysFont('ubuntu', 50)
                    message1 = my_font.render(msg, True, Color('white'))
                    screen.blit(message1, rect)
                    pygame.display.flip()
                    time_blocker()
                return completed_dozes
    
        screen.fill((200,100,100))
    
        rect = Rect(100,100, 10, 10)            
        msg = 'Time to take a doze!'
        my_font = pygame.font.SysFont('ubuntu', 50)
        message1 = my_font.render(msg, True, Color('black'))
        screen.blit(message1, rect)
        
        pygame.display.flip()
                
        pygame.time.wait(100)   

def app():

    #-------------------------Game Initialization-------------------------
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BG_COLOUR = 100, 200, 100

    pygame.init()
    pygame.mixer.init()
    
    screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    clock = pygame.time.Clock()

    curr_time = gmtime()
    
    time_blocker()
        
    completed_dozes = 0

    running = True

    #-----------------------------The Game Loop---------------------------
    while running:
        
        #Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == KEYDOWN:
                pass

            
        #Fill background colour
        screen.fill(BG_COLOUR)
        
        rect = Rect(50,100, 10, 10)
        msg = 'Number of dozes completed : ' + str(completed_dozes)
        my_font = pygame.font.SysFont('ubuntu', 50)
        message1 = my_font.render(msg, True, Color('black'))
        screen.blit(message1, rect)
        
        #pygame.draw.rect (screen, Color('black'), (350, 250, 100, 100))
        
        raw_time = gmtime()
        #if (raw_time.tm_min == 0 or raw_time.tm_min == 15 or raw_time.tm_min == 30 or raw_time.tm_min == 45) and raw_time.tm_sec == 0:  
        if raw_time.tm_sec == 0:
            completed_dozes = deadline(screen, completed_dozes)
            
        disp_time_min =raw_time.tm_min%15
        disp_time_min = 14-disp_time_min
        
        disp_time_sec = raw_time.tm_sec
        disp_time_sec = 59-disp_time_sec 
        
        time_rect = (300, 200, 10, 10)
        time = str(disp_time_min) + ':' + str(disp_time_sec)
        message2 = my_font.render(time, True, Color('black'))
        screen.blit(message2, time_rect)  
          
        #Flip the display buffer
        pygame.display.flip()

        #Delay
        pygame.time.wait(100)
app()
