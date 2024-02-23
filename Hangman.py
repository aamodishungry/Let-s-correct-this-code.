
import pygame
import sys
import random
from timeit import default_timer as timer


fps = 30
pygame.init()
width = 1200
height = 650
chances = 8
black = (12, 20, 10)
white = (255, 255, 200)
lightred = (255, 138, 128)
darklightred = (205, 41, 27)
lightblue = (97, 164, 255)
darklightblue = (31, 101, 201)
lightgrey = (66, 9, 88)
js = (216,66,66)
nn = (234,255,123)
textBoxSpace = 5
textBoxNumber = 0

def button(word,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))

    buttonText = pygame.font.Font("freesansbold.ttf",20)
    buttonTextSurf = buttonText.render(word, True, white)
    buttonTextRect = buttonTextSurf.get_rect()
    buttonTextRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(buttonTextSurf, buttonTextRect)




def winGame():
    global textBoxSpace, textBoxNumber, end, start
    end = timer()
    print("Time it took: ", end - start)
    timeTaken = (end - start)
    textBoxSpace = 5
    textBoxNumber = 0
    message = "Time taken: " + str(round(timeTaken)) + "s"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        button("Exit", (width / 2) - 50, 420, 100, 50, darklightred, lightred, quitGame)
        button("Play Again", (width / 2.025) - 50, 500, 120, 50, darklightred, lightred, hangman)

        largeText = pygame.font.SysFont("comicsansms", 75)
        TextSurf = largeText.render("You have won!", True, darklightred)
        TextRect = TextSurf.get_rect()
        TextRect.center = (width / 2, height / 2)
        screen.blit(TextSurf, TextRect)

        textSurf = largeText.render(message, True, darklightred)
        textRect = textSurf.get_rect()
        textRect.center = (width / 2, 200)
        screen.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(fps)

def endGame():
        global textBoxSpace, textBoxNumber, end, start
        end = timer()
        print("Time it took: ", end - start)
        timeTaken = (end - start)
        textBoxSpace = 5
        textBoxNumber = 0
        message = "Time taken: " + str(round(timeTaken)) + "s"
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            button("Exit", (width / 2) - 50, 420, 100, 50, darklightred, lightred, quitGame)
            button("Play Again", (width / 2.025) - 50, 500, 120, 50, darklightred, lightred, hangman)

            largeText = pygame.font.SysFont("comicsansms", 75)
            TextSurf = largeText.render("You have lost!", True, darklightred)
            TextRect = TextSurf.get_rect()
            TextRect.center = (width / 2, height / 2)
            screen.blit(TextSurf, TextRect)

            textSurf = largeText.render(message, True, darklightred)
            textRect = textSurf.get_rect()
            textRect.center = (width / 2, 200)
            screen.blit(textSurf, textRect)

            pygame.display.update()
            clock.tick(fps)
def quitGame():
    pygame.quit()
    sys.exit()

def unpause():
    global pause
    pause = False

def pause():
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf = largeText.render("Paused",True,black)
    TextRect = TextSurf.get_rect()
    TextRect.center = (width / 2, height / 2)
    screen.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill(nn)
        

        button("Continue",150,450,100,50,darklightred,lightred,unpause)
        button("Quit",550,450,100,50,darklightblue,lightblue)

        pygame.display.update()
        clock.tick(fps)

def textObjects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def main():
    global clock, screen, play
    play = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Hangman.Game.Play and win")

    while True:
        hangman()

def placeLetter(letter):
    global pick, pickSplit
    space = 10
    wordSpace = 0
    while wordSpace < len(pick):
        text = pygame.font.Font('freesansbold.ttf',40)
        if letter in pickSplit[wordSpace]:
            textSurf = text.render(letter,True,black)
            textRect = textSurf.get_rect()
            textRect.center = (((150)+space),(200))
            screen.blit(textSurf, textRect)
        wordSpace += 1
        space += 60

    pygame.display.update()
    clock.tick(fps)
        
def textBoxLetter(letter):
    global textBoxSpace, textBoxNumber
    if textBoxNumber <= 5:
        text = pygame.font.Font("freesansbold.ttf",40)
        textSurf = text.render(letter,True,black)
        textRect = textSurf.get_rect()
        textRect.center = (((105)+textBoxSpace),(350))
        screen.blit(textSurf, textRect)

    elif textBoxNumber <= 10:
        text = pygame.font.Font("freesansbold.ttf",40)
        textSurf = text.render(letter,True,black)
        textRect = textSurf.get_rect()
        textRect.center = (((105)+textBoxSpace),(400))
        screen.blit(textSurf, textRect)

    elif textBoxNumber <= 15:
        text = pygame.font.Font("freesansbold.ttf",40)
        textSurf = text.render(letter,True,black)
        textRect = textSurf.get_rect()
        textRect.center = (((105)+textBoxSpace),(450))
        screen.blit(textSurf, textRect)

    elif textBoxNumber <= 20:
        text = pygame.font.Font("freesansbold.ttf",40)
        textSurf = text.render(letter,True,black)
        textRect = textSurf.get_rect()
        textRect.center = (((105)+textBoxSpace),(500))
        screen.blit(textSurf, textRect)  
        
    pygame.display.update()
    clock.tick(fps)

def hangman():
    global textBoxSpace, textBoxNumber
    textBoxSpace = 5
    textBoxNumber = 0
    while play == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(js)
        space = 10
        textBoxSpace = 5
        
        text = pygame.font.Font("freesansbold.ttf",30)
        textSurf = text.render("Choose any option.",True,black)
        textRect = textSurf.get_rect()
        textRect.center = ((width/2),50)
        screen.blit(textSurf, textRect)

        button("Animals",330,100,100,70,black,lightgrey,Animal)
        button("Vehicles",480,100,100,70,black,lightgrey,Vehicle)
        button("Food",630,100,100,70,black,lightgrey,Food)
        button("Sports",780,100,100,70,black,lightgrey,Sport)
        
        text = pygame.font.Font("freesansbold.ttf",30)
        textSurf = text.render("For Hangman Game!",True,black)
        textRect = textSurf.get_rect()
        textRect.center = ((width/2),210)
        screen.blit(textSurf, textRect)
    
        
        
        pygame.draw.rect(screen,black,[425,550,100,10],2)
        pygame.draw.rect(screen, black, [525, 550, 100, 10], 2)
        pygame.draw.rect(screen, black, [625, 550, 100, 10], 2)
        pygame.draw.rect(screen, black, [475, 450, 10, 100], 2)
        pygame.draw.rect(screen, black, [475, 350, 10, 100], 2)
        pygame.draw.rect(screen, black, [475, 250, 10, 100], 2)
        pygame.draw.rect(screen, black, [475, 250, 150, 10], 2)
        pygame.draw.rect(screen, black, [575, 250, 100, 10], 2)
        pygame.draw.rect(screen, black, [575, 250, 10, 50], 2)
        
# Additional shapes
        pygame.draw.circle(screen, black, [580, 325], 30)
        pygame.draw.rect(screen, black, [575, 350, 10, 60])
        pygame.draw.rect(screen, black, [575, 410, 10, 60])
        pygame.draw.line(screen, black, [580, 375], [525, 395], 10)
        pygame.draw.line(screen, black, [580, 375], [625, 395], 10)
        pygame.draw.line(screen, black, [580, 465], [525, 485], 10)
        pygame.draw.line(screen, black, [580, 465], [625, 485], 10)

                 
        pygame.display.update()
        
        clock.tick(fps)

def hangmanGame(catagory,title):
    global pause, pick, pickSplit, textBoxSpace, textBoxNumber, start
    start = timer()
    chances = 8
    pick = random.choice(catagory)
    pickSplit = [pick[i:i+1] for i in range(0, len(pick), 1)]
    
    screen.fill(nn)
    
    wordSpace = 0
    space = 10
    while wordSpace < len(pick):
        text = pygame.font.Font("freesansbold.ttf",40)
        textSurf1 = text.render("_",True,black)
        textRect1 = textSurf1.get_rect()
        textRect1.center = (((150)+space),(200))
        screen.blit(textSurf1, textRect1)
        space = space + 60
        wordSpace += 1
            
    guesses = ''
    gamePlay = True
    while gamePlay == True:
        guessLett = ''

        if textBoxNumber == 5:
            textBoxSpace = 5
        if textBoxNumber == 10:
            textBoxSpace = 5
        if textBoxNumber == 15:
            textBoxSpace = 5

        pygame.draw.rect(screen, white, [970,15,150,30])
        text = pygame.font.Font("freesansbold.ttf",20)
        textSurf = text.render(("Chances: %s" % chances),False,black)
        textRect = textSurf.get_rect()
        textRect.topright = (1100,20)
        screen.blit(textSurf, textRect)

        textTitle = pygame.font.Font("freesansbold.ttf",40)
        textTitleSurf = textTitle.render(title,True,black)
        textTitleRect = textTitleSurf.get_rect()
        textTitleRect.center = ((width/2),50)
        screen.blit(textTitleSurf, textTitleRect)

        pygame.draw.rect(screen, black, [100,300,250,250],2)
        pygame.draw.rect(screen,black,[450,550,100,10])
        pygame.draw.rect(screen,black,[550,550,100,10])
        pygame.draw.rect(screen,black,[650,550,100,10])
        
        pygame.draw.rect(screen,black,[500,450,10,100])
        pygame.draw.rect(screen,black,[500,350,10,100])
        pygame.draw.rect(screen,black,[500,250,10,100])
        pygame.draw.rect(screen,black,[500,250,150,10])
        pygame.draw.rect(screen,black,[600,250,100,10])
        pygame.draw.rect(screen,black,[600,250,10,50])
        pygame.draw.line(screen,black,[505,505],[550,550],10)
        pygame.draw.line(screen,black,[550,250],[505,295],10)
        pygame.draw.line(screen,black,[505,505],[460,550],10)
        if chances == 7:
            pygame.draw.circle(screen,black,[605,325],30)
        elif chances == 6:
            pygame.draw.rect(screen,black,[600,350,10,60])
        elif chances == 5:
            pygame.draw.rect(screen,black,[600,410,10,60])
        elif chances == 4:
            pygame.draw.line(screen,black,[605,375],[550,395],10)
        elif chances == 3:
            pygame.draw.line(screen,black,[605,375],[650,395],10)
        elif chances == 2:
            pygame.draw.line(screen,black,[605,465],[550,485],10)
        elif chances == 1:
            pygame.draw.line(screen,black,[605,465],[650,485],10)
        
        button("Back",50,50,100,50,black,lightgrey,hangman)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                failed = 0
                print("Failed",failed)
                print("Chance", chances)
                
                if event.key == pygame.K_SPACE:
                    pause()
                    
                if event.key == pygame.K_ESCAPE:
                    gamePlay = False
                    
                if event.key == pygame.K_a:
#letter a
                    guessLett = guessLett + 'a'
                    guesses += guessLett
                    print("letter a guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('a')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()


                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('a')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                            
                if event.key == pygame.K_b:
#letter b
                    guessLett = guessLett + 'b'
                    guesses += guessLett
                    print("letter b guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('b')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('b')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_c:
#letter c
                    guessLett = guessLett + 'c'
                    guesses += guessLett
                    print("letter c guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('c')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('c')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_d:
#letter d
                    guessLett = guessLett + 'd'
                    guesses += guessLett
                    print("letter d guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('d')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('d')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_e:
#letter e
                    guessLett = guessLett + 'e'
                    guesses += guessLett
                    print("letter e guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('e')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('e')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_f:
#letter f
                    guessLett = guessLett + 'f'
                    guesses += guessLett
                    print("letter f guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('f')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('f')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_g:
#letter g
                    guessLett = guessLett + 'g'
                    guesses += guessLett
                    print("letter g guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('g')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('g')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_h:
#letter h
                    guessLett = guessLett + 'h'
                    guesses += guessLett
                    print("letter h guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('h')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('h')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_i:
#letter i
                    guessLett = guessLett + 'i'
                    guesses += guessLett
                    print("letter i guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('i')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('i')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_j:
#letter j
                    guessLett = guessLett + 'j'
                    guesses += guessLett
                    print("letter j guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('j')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        #gamePlay = False
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('j')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        #gamePlay = False
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_k:
#letter k
                    guessLett = guessLett + 'k'
                    guesses += guessLett
                    print("letter k guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('k')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('k')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_l:
#letter l
                    guessLett = guessLett + 'l'
                    guesses += guessLett
                    print("letter l guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('l')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('l')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_m:
#letter m
                    guessLett = guessLett + 'm'
                    guesses += guessLett
                    print("letter m guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('m')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('m')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_n:
#letter n
                    guessLett = guessLett + 'n'
                    guesses += guessLett
                    print("letter n guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('n')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        #gamePlay = False
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('n')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        #gamePlay = False
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_o:
#letter o
                    guessLett = guessLett + 'o'
                    guesses += guessLett
                    print("letter o guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('o')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('o')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_p:
#letter p
                    guessLett = guessLett + 'p'
                    guesses += guessLett
                    print("letter p guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('p')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('p')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_q:
#letter q
                    guessLett = guessLett + 'q'
                    guesses += guessLett
                    print("letter q guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('a')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('q')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_r:
#letter r
                    guessLett = guessLett + 'r'
                    guesses += guessLett
                    print("letter r guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('r')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('r')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_s:
#letter s
                    guessLett = guessLett + 's'
                    guesses += guessLett
                    print("letter s guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('s')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('s')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_t:
#letter t
                    guessLett = guessLett + 't'
                    guesses += guessLett
                    print("letter t guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('t')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('t')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_u:
#letter u
                    guessLett = guessLett + 'u'
                    guesses += guessLett
                    print("letter u guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1
                    if guessLett in pick:
                        placeLetter('u')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('u')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_v:
#letter v
                    guessLett = guessLett + 'v'
                    guesses += guessLett
                    print("letter v guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('v')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('v')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_w:
#letter w
                    guessLett = guessLett + 'w'
                    guesses += guessLett
                    print("letter w guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('w')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('w')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_x:
#letter x
                    guessLett = guessLett + 'x'
                    guesses += guessLett
                    print("letter x guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1
                    if guessLett in pick:
                        placeLetter('x')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('x')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_y:
#letter y
                    guessLett = guessLett + 'y'
                    guesses += guessLett
                    print("letter y guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('y')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('y')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()
                if event.key == pygame.K_z:
#letter z
                    guessLett = guessLett + 'z'
                    guesses += guessLett
                    print("letter z guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('z')
            
                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('z')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was",pick)
                        endGame()
                    elif chances >= 0:
                        print(pick)
                        winGame()

        pygame.display.update()
        clock.tick(fps)

    pygame.display.update()
    clock.tick(fps)

def Animal():
    animal = [
    "Lion", "Tiger", "Bear", "Elephant", "Giraffe", "Zebra", "Cheetah", "Rhino", "Hippopotamus", "Gorilla",
    "Chimpanzee", "Orangutan", "Leopard", "Jaguar", "Wolf", "Fox", "Coyote", "Deer", "Moose", "Elk",
    "Bison", "Antelope", "Gazelle", "Wildebeest", "Hyena", "Jackal", "African Elephant", "Asian Elephant",
    "Panda", "Koala", "Kangaroo", "Wallaby", "Wombat", "Platypus", "Tasmanian Devil", "Dingo", "Red Kangaroo",
    "Gray Kangaroo", "Red Panda", "Polar Bear", "Grizzly Bear", "Black Bear", "Brown Bear", "Kodiak Bear",
    "Panda Bear", "Sun Bear", "Moon Bear", "Sloth Bear", "Spectacled Bear", "Andean Bear", "Giant Panda",
    "Bengal Tiger", "Siberian Tiger", "Sumatran Tiger", "Indochinese Tiger", "Malayan Tiger", "South China Tiger",
    "Caspian Tiger", "Javan Tiger", "Bali Tiger", "Barbary Lion", "Cape Lion", "European Cave Lion", "American Lion",
    "Asiatic Lion", "Barbary Macaque", "Rhesus Macaque", "Japanese Macaque", "Bonobo", "Western Lowland Gorilla",
    "Eastern Lowland Gorilla", "Mountain Gorilla", "Bornean Orangutan", "Sumatran Orangutan", "Tapanuli Orangutan",
    "Common Chimpanzee", "Bonobo Chimpanzee", "Pygmy Chimpanzee", "Black Leopard", "Snow Leopard", "Clouded Leopard",
    "Persian Leopard", "Amur Leopard", "Arabian Leopard", "Indian Leopard", "Sri Lankan Leopard", "Asiatic Cheetah",
    "Northwest African Cheetah", "Northeast African Cheetah", "Southern African Cheetah", "Leopard", "Panthera pardus",
    "Panthera onca", "Panthera leo", "Panthera tigris", "Panthera uncia", "Panthera hybrid", "Panthera", "African Lion",
    "Persian Lion", "TibetanAntelope", "Mongolian Gazelle", "Tibetan Gazelle", "Goitered Gazelle", "Dama Gazelle",
    "Arabian Oryx", "ScimitarOryx", "Addax", "Slender-Horned Gazelle", "African Forest Elephant", "African Bush Elephant",
    "Indian Elephant", "SriLankan Elephant", "Sumatran Elephant", "Borneo Elephant", "Pygmy Elephant", "Forest Elephant",
    "European Bison", "AmericanBison", "Steppe Bison", "Wood Bison", "Ancient Bison", "Highland Bison", "Lowland Bison",
    "Yak", "Wisent", "Bisononasus", "Buffalo", "Bison bison", "B. bison bison", "athabascae", "B. b. bison",
    "caucasicus", "groenlandicus", "hamiltonii", "montana", "peninsularis", "B. b. phalanx",
    "plains bison", "ssp.", "tarnobrzegensis", "urochs", "Bos bison", "Bison priscus",
    "Bison antiquus", "Bison latifrons", "Bison occidentalis", "North American Bison"
]

    print("animal")
    title = "Animals"
    hangmanGame(animal,title)

def Vehicle():
    vehicle = [
    "Car", "Truck", "Bus", "Motorcycle", "Bicycle", "Scooter", "Van", "SUV", "Minivan", "Ambulance",
    "Firetruck", "Police Car", "Taxi", "Limousine", "RV", "Camper", "ATV", "Snowmobile", "Jet Ski",
    "Boat", "Yacht", "Ship", "Ferry", "Submarine", "Airplane", "Helicopter", "Glider", "Paraglider",
    "Hot Air Balloon", "Zeppelin", "Space Shuttle", "Rocket", "Satellite", "Lunar Rover", "Mars Rover",
    "Hovercraft", "Hydrofoil", "Catamaran", "Trimaran", "Sailboat", "Speedboat", "Rowboat", "Canoe", "Kayak",
    "Raft", "Barge", "Cargo Ship", "Container Ship", "Oil Tanker", "Fishing Boat", "Tugboat", "Cruise Ship",
    "Gondola", "Pedicab", "Rickshaw", "Horse and Carriage", "Stagecoach", "Covered Wagon", "Buggy", "Tractor",
    "Combine Harvester", "Bulldozer", "Excavator", "Backhoe Loader", "Dump Truck", "Concrete Mixer", "Crane",
    "Forklift", "Skid Steer Loader", "Wheel Loader", "Grader", "Road Roller", "Asphalt Paver", "Pneumatic Roller",
    "Steamroller", "Compactor", "Cement Truck", "Flatbed Truck", "Tow Truck", "Garbage Truck", "Semi-Trailer Truck",
    "Tanker Truck", "Box Truck", "Refrigerator Truck", "Dump Truck", "Concrete Pump Truck", "Fire Engine",
    "Aerial Fire Apparatus", "Water Tender", "Airport Crash Tender", "Aircraft Rescue and Firefighting", "Pumper",
    "Turntable Ladder", "Quint", "Light Rescue Vehicle", "Heavy Rescue Vehicle", "Tactical Response Vehicle",
    "Ambulance", "Type I Ambulance", "Type II Ambulance", "Type III Ambulance", "Type IV Ambulance",
    "Type V Ambulance", "Mobile Intensive Care Unit", "Bariatric Ambulance", "Air Ambulance", "Fire Ambulance",
    "Motorcycle Ambulance", "Helicopter Ambulance", "Highway Patrol Vehicle", "K-9 Unit Vehicle", "SWAT Vehicle",
    "Armored Vehicle", "Cruiser", "Interceptor", "Traffic Car", "Supervisor Vehicle", "Unmarked Vehicle",
    "Marked Vehicle", "Undercover Vehicle", "Patrol Car", "Search and Rescue Vehicle", "Buggy", "Dune Buggy",
    "Beach Buggy", "Railcar", "Train", "Tram", "Subway", "Monorail", "Maglev Train", "Bullet Train",
    "High-Speed Train", "Trolleybus", "Tram", "Streetcar", "Bus Rapid Transit", "Light Rail Transit", "Metro",
    "Cable Car", "Funicular", "Gondola Lift", "Chairlift", "Aerial Tramway", "Cableway", "Elevator", "Escalator",
    "Moving Walkway", "Segway", "Hoverboard", "Electric Skateboard", "Electric Scooter", "Electric Bicycle",
    "Electric Motorcycle", "Electric Car", "Hybrid Car", "Hydrogen Car", "Plug-In Hybrid Car", "Autonomous Car",
    "Self-Driving Car", "Driverless Car", "Flying Car", "Electric Plane", "Solar-Powered Vehicle", "Human-Powered Vehicle",
    "Battery Electric Vehicle", "Fuel Cell Electric Vehicle", "Hybrid Electric Vehicle", "Plug-In Hybrid Electric Vehicle",
    "Autonomous Vehicle", "Self-Driving Vehicle", "Driverless Vehicle", "Electric Train", "Maglev Train",
    "Monorail Train", "High-Speed Train", "Bullet Train", "Tram", "Streetcar", "Subway Train", "Metro Train",
    "Diesel Train", "Steam Train", "Electric Locomotive", "Diesel Locomotive", "Electric Tram", "Trolleybus",
    "Electric Bus", "Hybrid Bus", "Electric Trolleybus", "Double-Decker Bus", "Coach Bus", "Tour Bus", "School Bus",
    "City Bus", "Airport Shuttle", "People Mover", "Train", "Carriage", "Wagon", "Engine", "Caboose",
    "Freight Car", "Boxcar", "Tank Car", "Flatcar", "Gondola Car", "Hopper Car", "Refrigerator Car",
    "Passenger Car", "Sleeping Car", "Dining Car", "Observation Car", "Bar Car", "Control Car", "Baggage Car",
    "Mail Car", "Postal Car", "Guard's Van", "Cab Car", "Driving Van Trailer", "Dining Car", "Panoramic Car",
    "Express Car", "Baggage Car", "Parlor Car", "Sleeper Car", "Pullman Car", "Day Coach", "Convertible Coach",
    "Tourist Coach", "Observation Coach", "Service Car", "Buffet Car", "Lounge Car", "Staff Car", "Kitchen Car",
    "Baggage Van", "Cargo Van", "Box Van", "Refrigerated Van", "Tank Van", "Covered Van", "Flatbed Van",
    "Mobile Workshop", "Mail Van", "Postal Van", "Emergency Van", "Armored Van", "ATV", "Snowmobile", "Dirt Bike",
    "Quad Bike", "Jet Ski", "Water Scooter", "Snow Scooter", "Mountain Bike", "Road Bike", "BMX Bike", "Cruiser Bike",
    "Touring Bike", "Tandem Bike", "Recumbent Bike", "Cargo Bike", "Racing Bike", "Electric Bike", "Trike", "Tricycle",
    "Recumbent Trike", "Cargo Trike", "Electric Trike", "Mountain Trike", "Recumbent Trike", "Ice Cream Truck",
    "Food Truck", "Coffee Truck", "Hot Dog Truck", "Taco Truck", "Burger Truck", "Pizza Truck", "Fruit Truck",
    "Vegetable Truck", "Fish Truck", "Meat Truck", "Dessert Truck", "Cookie Truck", "Candy Truck", "Cupcake Truck",
    "Bakery Truck", "Donut Truck", "Gelato Truck", "Frozen Yogurt Truck", "Ice Cream Cart", "Food Cart",
    "Hot Dog Cart", "Taco Cart", "Burger Cart", "Pizza Cart", "Fruit Cart", "Vegetable Cart", "Fish Cart",
    "Meat Cart", "Dessert Cart", "Cookie Cart", "Candy Cart", "Cupcake Cart" ]

    print("vehicle")
    title = "Vehicles"
    hangmanGame(vehicle,title)
    
def Food():
    food = [
    "pizza"]

    print("food")
    title = "Foods"
    hangmanGame(food,title)
    
def Sport():
    sport = [
    "Football", "Basketball", "Baseball", "Soccer", "Tennis", "Golf", "Rugby", "Cricket", "Hockey", "Volleyball",
    "Table Tennis", "Badminton", "Boxing", "Martial Arts", "Wrestling", "Swimming", "Diving", "Water Polo", "Synchronized Swimming",
    "Rowing", "Canoeing", "Kayaking", "Sailing", "Surfing", "Windsurfing", "Kitesurfing", "Paddleboarding", "Fishing", "Ice Hockey",
    "Field Hockey", "Lacrosse", "Polo", "Archery", "Shooting", "Fencing", "Gymnastics", "Trampoline", "Artistic Gymnastics",
    "Rhythmic Gymnastics", "Skiing", "Snowboarding", "Cross-Country Skiing", "Alpine Skiing", "Freestyle Skiing", "Ski Jumping",
    "Nordic Combined", "Biathlon", "Bobsleigh", "Skeleton", "Luge", "Speed Skating", "Figure Skating", "Ice Dancing",
    "Ice Skating", "Short Track Speed Skating", "Long Track Speed Skating", "Curling", "Bandy", "Broomball", "Handball",
    "Pickleball", "Racquetball", "Squash", "Futsal", "Ultimate Frisbee", "Dodgeball", "Gaelic Football", "Hurling", "Camogie",
    "Australian Rules Football", "American Football", "Flag Football", "Canadian Football", "Arena Football", "Touch Football",
    "Rugby League", "Rugby Union", "Sevens Rugby", "Tug of War", "Kickball", "Softball", "Rounders", "Cricket", "Baseball",
    "Slow Pitch Softball", "Fast Pitch Softball", "Beach Volleyball", "Sepak Takraw", "Footvolley", "Bossaball", "Kin-Ball",
    "Sitting Volleyball", "Snow Volleyball", "Wheelchair Basketball", "Wheelchair Rugby", "Wheelchair Tennis", "Wheelchair Fencing",
    "Goalball", "Para Ice Hockey", "Sledge Hockey", "Powerlifting", "Weightlifting", "Bodybuilding", "Strongman", "Arm Wrestling",
    "CrossFit", "Parkour", "Obstacle Course Racing", "Triathlon", "Ironman", "Decathlon", "Pentathlon", "Heptathlon", "Biathlon",
    "Modern Pentathlon", "Aquathlon", "Duathlon", "Tetrathlon", "Quadrathlon", "Surf Lifesaving", "Lifesaving", "Surf Skiing",
    "Surf Boat Rowing", "Surf Ironman", "Surf Swimming", "Board Paddling", "Beach Flags", "Beach Sprint", "Beach Relay",
    "Beach Run", "Beach Wrestling", "Surfing", "Bodyboarding", "Kiteboarding", "Windsurfing", "Surf Kayaking", "Surf Skiing",
    "Wakesurfing", "Wakeskating", "Wakeboarding", "Water Skiing", "Ski Racing", "Skijoring", "Dog Sledding", "Snowmobiling",
    "Snowkiting", "Ice Climbing", "Mountaineering", "Rock Climbing", "Bouldering", "Sport Climbing", "Traditional Climbing",
    "Ice Climbing", "Indoor Climbing", "Alpine Climbing", "Highlining", "Slacklining", "Bungee Jumping", "Paragliding", "Hang Gliding",
    "Skydiving", "Wingsuit Flying", "BASE Jumping", "Cliff Diving", "Canyoning", "Caving", "Spelunking", "Scuba Diving", "Freediving",
    "Snorkeling", "Spearfishing", "Underwater Hockey", "Underwater Rugby", "Underwater Target Shooting", "Apnea Competition",
    "Target Archery", "Field Archery", "3D Archery", "Crossbow Archery", "Flight Archery", "Run Archery", "Skateboarding",
    "Longboarding", "Street Skateboarding", "Park Skateboarding", "Vert Skateboarding", "Freestyle Skateboarding", "Slalom Skateboarding",
    "Downhill Skateboarding", "Off-Road Skateboarding", "Cruising Skateboarding", "Freeride Skateboarding", "Surf Skateboarding",
    "Snowboarding", "Freestyle Snowboarding", "Alpine Snowboarding", "Snowboard Racing", "Freeride Snowboarding", "Freecarve Snowboarding",
    "Slopestyle Snowboarding", "Halfpipe Snowboarding", "Big Air Snowboarding", "Backcountry Snowboarding", "Splitboarding", "Snowsurfing",
    "Snowskating", "Snowmobiling", "Skiing", "Alpine Skiing", "Cross-Country Skiing", "Freestyle Skiing", "Nordic Skiing", "Backcountry Skiing",
    "Telemark Skiing", "Ski Mountaineering", "Ski Racing", "Ski Jumping", "Ski Cross", "Ski Ballet", "Ski Freeride", "Ski Freestyle", "Ski Halfpipe",
    "Ski Big Air", "Ski Slopestyle", "Ski Moguls", "Ski Dual Moguls", "Ski Downhill", "Ski Super-G", "Ski Giant Slalom", "Ski Slalom",
    "Ski Speed Skiing", "Ski Biathlon", "Ski Bobsleigh", "Ski Cross-Country Biathlon", "Ski Orienteering", "Ski Jöring", "Ski Skijöring",
    "Ski Touring", "Ski Trekking", "Ski Mountaineering", "Ski Orienteering", "Ski Jöring", "Ski Skijöring", "Ski Touring", "Ski Trekking",
    "Ski Mountaineering", "Ski Paragliding", "Ski Speed Riding", "Ski Mountaineering", "Ski Orienteering", "Ski Jöring", "Ski Skijöring",
    "Ski Touring", "Ski Trekking", "Ski Mountaineering", "Ski Orienteering", "Ski Jöring", "Ski Skijöring", "Ski Touring", "Ski Trekking",
    "Ski Mountaineering", "Ski Paragliding", "Ski Speed Riding", "Skijöring", "Ski Jöring", "Ski Skijöring", "Ski Touring", "Ski Trekking",
    "Ski Mountaineering", "Ski Orienteering", "Ski Jöring", "Ski Skij" ]

    print("sport")
    title = "Sports"
    hangmanGame(sport,title)
 
    
if __name__ == '__main__':
    main()
            
