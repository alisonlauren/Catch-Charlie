#importing pygame and initializing game as well
import pygame
pygame.init()
#importing time, random and math function
import time  
import random
import math
#setting the size of the window, setting the caption and starting the "time" start on the game
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('CATCH CHARLIE, ASAP!!!')
clock = pygame.time.Clock()

###PRESENTATION QUESTIONS
#1. Most challenging.... line 54-72. and line 185. the logic was hard to grasp, and additionally my photos were not all sized the same.
#2. Most enjoyed..... but all the challenge was worth it to get to personalize it
#3. Next time.... a) get familair with pygame first b) LITERALLY ANY OTHER MUSIC




#uploading all my images
background_image = pygame.image.load('images/neighstreet.jpg').convert_alpha()
Ali_image = pygame.image.load('images/ali.png').convert_alpha()
charlie_image = pygame.image.load('images/charlie.png').convert_alpha()
car_image = pygame.image.load('images/redcar.png'). convert_alpha()
#reconstructing my background image
background_image = pygame.image.load('images/neighstreet.jpg')
background_image = pygame.transform.scale(background_image, (500, 500))
#reconstructing ali image
Ali_image = pygame.image.load('images/ali.png')
Ali_image = pygame.transform.scale(Ali_image, (70, 165))
#reconstructing charlie image
charlie_image = pygame.image.load('images/charlie.png')
charlie_image = pygame.transform.scale(charlie_image, (70, 120))
#reconstructing car image
car_image = pygame.image.load('images/redcar.png')
car_image = pygame.transform.scale(car_image, (70, 120))

###if player wins, a func that will called later, play this horrible music :(
player_wins = pygame.mixer.Sound ('sounds/win.wav')
###loading it to my code
pygame.mixer.music.load('sounds/music.wav')
#unfortuntely play this music
##well you lost so (variable will be used later on)...
lose_sound = pygame.mixer.Sound ('sounds/lose.wav')
pygame.mixer.music.play()

class Ali:
        def __init__ (self, width, height):
            self.timer = 0
            self.direction = 2
            self.x = width/2
            self.y = height/2
            self.caught = False
        def change_direction(self, width, height, xlane, ylane):
            #this took a tremendous amount of playing with since i have funny sizes for my images
            #if Ali's width + 125 pixels is greater than the width of the gaming window,
            #then width is equal to width minus -125. thus essentially never letting it be equal to
            #anything greater than the 500/500 window. 
            if self.x + 125 > width:
                self.x = width - 125
            #else/if Ali's width is less than 0 on the x-axis then it equals to zero, meaning
            #Ali cannot go beyond the 0 point on the x axis
            elif self.x < 0:
                self.x = 0
            #if Ali's height is less than 0 on the y-axis then continue to keep it equal to zero, aka
            #Alicannot go beyond the 0 point on the y axis
            if self.y < 0:
                self.y = 0
            #else/if Ali's height + 200 is greater than the height of the window, then
            #ensure her new position never exceeds the furthest point on the y axis
            elif self.y + 200 > height:
                self.y = height - 200
            #giving ability to move in all direction, this will be keyed in later
            ###if on the yaxis and going up, then on the xaxis add some opposite direction,
            if ylane == 0:
                self.y = self.y - self.direction
            ###if on the yaxis and going down, then on the xaxis add some opposite direction
            elif ylane == 1:
                self.y = self.y + self.direction
            ####if on the xaxis and going up, then on the yaxis and some opposite direction
            if xlane == 0:
                self.x = self.x + self.direction
            ####if on the xaxis and going down, then on the yaxis add some direction(opposite)
            elif xlane == 1:
                self.x = self.x - self.direction
class Antagonist:
    def __init__ (self, width, height):
        self.xlane = random.randint(0, 1)
        self.ylane = random.randint(0, 1)
        self.timer = 2
        self.direction = 3
        self.x = width
        self.y = height
        self.caught = False

    def change_direction(self, width, height):
   #*****CHARLIE/PROTAG MOVES RIGHT****** 
        self.x += -2
        if self.x < 0:
            self.x = 500
    #*****CHARLIE/PROTAG MOVES LEFT*******
        self.x += 2
        if self.x > 500:
           self.x = 0
    #*****CHARLIE/PROTAG MOVES UP********
        self.y += -2
        if self.y < 0:
            self.y = 500
    #******CHARLIE/PROTAG MOVES DOWN******
        self.y += 2
        if self.y > 500:
            self.y = 0
    #********activates the diagonal movement#######
        ####if on the xaxis and going up, then on the yaxis and some opposite direction
        if self.xlane == 0:
            self.y = self.y + self.direction 
        ####if on the xaxis and going down, then on the yaxis add some direction(opposite)
        elif self.xlane == 1:
            self.y = self.y - self.direction
        ###if on the yaxis and going up, then on the xaxis add some opposite direction
        if self.ylane == 0:
            self.x = self.x - self.direction
        ###if on the yaxis and going down, then on the xaxis add some opposite direction
        elif self.ylane == 1:
            self.x = self.x + self.direction
       

class Charlie(Antagonist):
    pass
class Cars(Antagonist):
    pass

def main():
    ###Could have set it to classic 500,500 but i felt like my background image really needed more space
    width = 550
    height = 550

    ###instead of calling my classes I can use this instead. creating them as variables.
    charlie = Antagonist(width, height)
    player = Ali(width, height)
    car1 = Antagonist(width, height)
    car2 = Antagonist(width, height)
    car3 = Antagonist(width, height)
    ###setting the font, and asking if they want to chase the pup again in white
    f = pygame.font.Font(None, 35)
    surf = f.render("Drop the leash?PRESS RETURN", 10, (255, 0, 255))
    surf_losegame = f.render("Try again? PRESS RETURN.", 1, (255,0,255))
   

    ####Game logic, while stop_game is equal to false......
    stop_game = False
    ##while the game has not stopped
    while not stop_game:
        ##calling the function from earlier, to change direction, i also edited
        ###the images at the top of the code to set their visual height in the game
        charlie.change_direction(width, height)
        car1.change_direction(width, height)
        car2.change_direction(width, height)
        car3.change_direction(width, height)
        ###must run this for events, (aka, anytime user pushes anything)
        for event in pygame.event.get():
        ###the game will only quit once stop_game is equal to true (with closing the tab)
            if event.type == pygame.QUIT:
                stop_game = True
        #basically just establishing a starting position        
        xlane = 4
        ylane = 4
        #if right key gets pressed move in the 0 direction aka xaxis
        key = pygame.key.get_pressed()
        if key [pygame.K_RIGHT]: 
            xlane = 0
        #if the left key gets pressed mmove in the 1 directoin aka xaxis
        if key [pygame.K_LEFT]:
            xlane = 1
        #if the up key gets pressed move it up on the yaxis
        if key [pygame.K_UP]:
            ylane = 0
        #if the down key get's pressed move it down on the yaxis
        if key [pygame.K_DOWN]:
            ylane = 1
        ###using this incredible formula to calcuate distance on step 14
        ###given that an image is 32 pixels, mine are not and I had to play with this
        ###i made the formula relevent to 50 pixels because i was using large photos
        if math.sqrt((player.x - charlie.x)**2 + (player.y - charlie.y)**2) <= 60:
            charlie.caught = True  
            player_wins.play()
        if math.sqrt((player.x - car1.x)**2 + (player.y - car1.y)**2) <= 90:
            player.caught = True
            lose_sound.play()
        if math.sqrt((player.x - car2.x)**2 + (player.y - car2.y)**2) <= 90:
            player.caught = True
            lose_sound.play()
        if math.sqrt((player.x - car3.x)**2 + (player.y - car3.y)**2) <= 90:
            player.caught = True
            lose_sound.play()
       
        ###if key return gets pressed, (after charlie get's caught of course )
        if key [pygame.K_RETURN] and charlie.caught:
            charlie.caught = False #now it would reset that charlie is not caught.......
            ####and send charlie back to random-ville
            charlie.x = random.randint(0, width)
            charlie.y = random.randint(0, height)
        if key [pygame.K_RETURN] and player.caught or car1.caught or car2.caught or car3.caught:
            player.caught = False
            #charlie.caught = False
            charlie.x = random.randint(0, width)
            charlie.y = random.randint(0, height)
        
        ###justing calling the function for the player, aka ali, get to steppin'   
        player.change_direction(width, height, xlane, ylane)
        #####drawing the background, setting the backround image
        screen.blit(background_image, [0, 0])
        if not player.caught:
            screen.blit(Ali_image, [player.x, player.y])
        if player.caught:
            screen.blit(surf_losegame, [width/7, height/2])
        ###drawing ali in to the mix, i belive the rest is confirming the x and y axis of the images
        #screen.blit(Ali_image, [player.x, player.y])
        screen.blit(car_image, [car1.x, car1.y])
        screen.blit(car_image, [car2.x, car2.y])
        screen.blit(car_image, [car3.x, car3.y])
        ##if charlie is not caught, let that boy run to his hearts content
        if not charlie.caught:
            screen.blit(charlie_image, [charlie.x, charlie.y])
        ###if charlie is caught, boof charlie is gone gone for a second
        if charlie.caught:
            screen.blit(surf, [width/5, height/2])

        # Gaming display
        pygame.display.update()
        charlie.timer += clock.tick(60)
        #I know the instructions called for 2 seconds(2000), but i want it to be hard to get charlie like it was in real life.
        if charlie.timer >= 500:
            charlie.timer = 0
        ###for all of the coordinates used by the Antagonists, make sure they are random, range set for 0-3
            charlie.xlane = random.randint(0, 3)
            charlie.ylane = random.randint(0, 3)
            car3.xlane = random.randint(0, 3)
            car3.ylane = random.randint(0, 3)
            car2.xlane = random.randint(0, 3)
            car2.ylane = random.randint(0, 3)
            car3.xlane = random.randint(0, 3)
            car3.ylane = random.randint(0, 3)





    pygame.quit()

if __name__ == '__main__':
    main()
