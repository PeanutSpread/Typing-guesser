# importing pygame and time along with initiating it.
import pygame
import time
pygame.init()

# A class for allowing images to be animated with ease from sprite sheets.
class anim(object):
    
    # Getting the information required for the entire class.
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name)
    
    # Making part of the original sprite sheet its own message.
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]) 
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0,0,0))
    
        # Returning the image.
        return image

# Setting up the game window.
SIZE = (400,600)
screen = pygame.display.set_mode(SIZE)
myClock = pygame.time.Clock()
pygame.mouse.set_visible(True)

# Setting up the the images to be used in animations or as buttons
Quit = pygame.image.load('Power_Button1.png')
Quit_Pressed = pygame.image.load('Power_Button2.png')
Background = anim('Text_Background.png')
Back = [Background.get_image(0,0,400,600),Background.get_image(400,0,400,600),Background.get_image(800,0,400,600),Background.get_image(1200,0,400,600),Background.get_image(1600,0,400,600),Background.get_image(2000,0,400,600),Background.get_image(2400,0,400,600),Background.get_image(2800,0,400,600)]
# opening the text file
Words = open("dict.txt", "r")

#initiating variables
lister = [] # used to load in the words from the text file
listing = [] # used to put the words and the amount of times they apear into one list
final = ["stop"] # used to find the order of the words that have the same amount of appearences
most = [] # used to order what final gathers into a complete list in order
letters = "" # used to match the input with the data gathered on words
string = "|" # used for showing input, geetting it and sending it back into the txt file
sentence = "" # used to create the sentence that shows all the words
last = "" # used to make sure that the user has changed his input
runs = 0 # used to make sure that all the words are in the most list
z = 0 # used to make animation frames visible
timer = 0 # used to make sure that the backspace doesent go too fast
state = 0 # used for putting the specific amount of words required
fonty = pygame.font.SysFont("Impact",20) # used for making the text font
delete = False # used to allow the holding down of the backspace
safe = False # used ro determine if the program can run without getting an error due to the inclusion of a strig in the wrong spot of a list
redo = True # used to allow the re-read of the text file
run = True # main run loop
rend = fonty.render(string, True, (0,0,0)) # used to make it possible for string to apear on screen
rend4 = fonty.render(sentence, True, (0,0,0)) # used to make it possible for scentence to apear on screen

# the start of the main run loop
while run == True:
    
    # used to gather the words into a list
    if redo == True:
        while True:
            text = Words.readline()
            text = text.rstrip("\n")  
            if text=="": 
                break
            lister.append(text)
    redo = False

    # making a list that holds words and the amount of times that word appears
    if safe == True:
        for i in range (0,len(lister)):
            wording = lister[i]
            if wording not in listing:
                final = []
                listing.append(wording.lower())
                listing.append(lister.count(wording))        
        
        # making sure that there are no repeats in the list and it is in order
        letters = string[:-1]
        letters = letters.lower()
        if safe == True:
            if final != "stop":
                for i in range (1,len(listing),2):
                    most.append(listing[i])
                    most.sort(reverse = True)
                    if runs < most[0]:
                        runs = most[0]
                    most = []
                
                # adding all the lists for each individual list created above
                for l in range(1,runs+1):
                    for i in range (0,len(listing),2):
                        if letters == listing[i][:len(letters)] and listing[i] not in most:
                            if final == []:
                                final = []
                                final.append(listing[i])
                                final.append(listing[i+1])            
                            elif listing[i+1] > final[1]:
                                final = []
                                final.append(listing[i])
                                final.append(listing[i+1]) 
                            elif listing[i+1] == final[1]:
                                final.append(listing[i])
                                final.append(listing[i+1])
                    for i in range (0,len(final)):
                        most.append(final[i])
                    final = [] 
    
    safe = False
    
    # getting the input from the keyboard and mouse
    for event in pygame.event.get():
        delete = False
        if event.type == pygame.KEYDOWN:
            
            # the backspace button
            if event.key == 8:
                delete = True
                safe = True
            
            # the escape key
            elif event.key == 27:
                sentence = ""
            
            # the return key and saving the wordinto the text file.
            elif event.key == 13:
                Words.close()
                Words = open("dict.txt", "a")
                Words.write(("\n"+string[:-1]))
                Words.close()
                Words = open("dict.txt", "r")
                if len(sentence) > 0:
                    sentence += " " + string[:-1]
                elif len(sentence) < 30:
                    sentence += string[:-1]
                if len(sentence) > 30:
                    sentence = sentence[:27] + "..."
                string = "|"
                redo = True
                safe = True
                num1 = "" 
                num2 = "" 
                num3 = ""
                lister = []
                listing = []
            
            # allowing the letters on the keyboard to register
            else:
                if event.key >= 97 and event.key <= 122 or event.key >= 48 and event.key <= 57 or event.key == 32 or event.key == 45 or event.key == 44 or event.key == 45 or event.key == 46 or event.key == 47:
                    if len(string) < 26:
                        string = string[:-1]
                        string += str(chr(event.key) + "|")
                        safe = True
        
        # mouse detection
        mouse = pygame.mouse.get_pos()
        x = mouse[0]
        y = mouse[1]
                
        # used to determine whether or not a word has been clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if x <= 124 and x >=5 and y <= 394 and y >= 305:
                if state == 1 or state == 2 or state == 3:
                    string = option1 + "|"
            if x <= 264 and x >=135 and y <= 394 and y >= 305:
                if state == 1 or state == 2:
                    string = option2  + "|"
            if x <= 394 and x >=275 and y <= 394 and y >= 305:
                if state == 1:
                    string = option3 + "|"
            # power button
            if x <= 400 and x >=350 and y <= 50 and y >= 0:
                run = False

    # used to time the animations for the background         
    timer += 1
    if timer % 4 == 0: 
        if z == 7:
            z = 0
        else:
            z += 1
    
    # used to allow the delete button to be held down
    if delete == True:
        if timer % 8 == 0:
            string = string[:-2]
            string += "|"
    
    # drawing the background and input text and sentence
    screen.blit(Back[z],(0,0))
    screen.blit(rend,(60,485))   
    screen.blit(rend4,(40,135))

    #updating the text
    rend = fonty.render(string, True, (0,0,0))
    rend4 = fonty.render(sentence, True, (0,0,0))
    

    # determining how many words apear along with asigning the top 3/2/1 word(S) that will apear to other variable to be kept.
    if len(most) > 0:
        if len(most) >= 6:
            option1 = most[0]
            option2 = most[2]
            option3 = most[4]
            num1 = " " + str(most[1])
            num2 = " " + str(most[3])
            num3 = " " + str(most[5])            
            state = 1
        elif len(most) == 4:
            state = 2
            option1 = most[0]
            option2 = most[2]
            num1 = " " + str(most[1])
            num2 = " " + str(most[3])
        elif len(most) == 2:
            state = 3
            option1 = most[0]
            num1 = " " + str(most[1])      
    
    # the indication of where the cursor is
    if string == "|" or safe == True:
        state = 0
    
    # putting the text on screen
    if state == 1:
        rend1 = fonty.render(option1 + num1, True, (0,0,0))
        rend2 = fonty.render(option2 + num2, True, (0,0,0))
        rend3 = fonty.render(option3 + num3, True, (0,0,0))
        screen.blit(rend1,(5,335))  
        screen.blit(rend2,(135,335))
        screen.blit(rend3,(275,335))  
    elif state == 2:
        rend1 = fonty.render(option1 + num1, True, (0,0,0))
        rend2 = fonty.render(option2 + num2, True, (0,0,0))
        screen.blit(rend1,(5,335))  
        screen.blit(rend2,(135,335))      
    elif state == 3:
        rend1 = fonty.render(option1 + num1, True, (0,0,0))
        screen.blit(rend1,(5,335))     
    
    # changing the picture based off mouse location
    if x <= 400 and x >=350 and y <= 50 and y >= 0:
        screen.blit(Quit_Pressed,(350,0))    
    else:
        screen.blit(Quit,(350,0))      

    # frame rate and drawing on screen
    myClock.tick(120)
    pygame.display.flip()
    
    # reseting the list that will cause an error if it is restarted without being clear
    most = [] 

# closing the down all the functions
Words.close()
pygame.quit()