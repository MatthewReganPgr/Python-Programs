#201278659 Regan_Matthew-CA05
#11/2017
#Hangman game

import random
import re

#Declaring variables
animalList = 0
furnitureList = 0
foodList = 0
guesses = 0
correctGuesses = 0
incorrectGuesses = 0
remainingGuesses = 0
previousGuesses = 0
emptyWord = 0
finalGuess = 0
letterOccurance = 0
indexOfGuess = 0


#List of all possible words that could occur when the game is run
animalList = ["SNAKE","DOG","ELEPHANT","MONKEY","HORSE","SHEEP","MOOSE","ARMIDILLO","TIGER"]
wordChoice = (random.choice(animalList))    #A single element from the above list is randomly chosen



def hangMan():
    remainingGuesses = (len(wordChoice))
    correctGuess = []
    incorrectGuess = []     #Declaring value of upcoming lists
    previousGuesses = []
    emptyWord = []
    i = 0
    j = 0
    k = 0
    for j in range (0, len(wordChoice)): #An underscore is printed for every letter in the chosen word
        emptyWord.append("_")
    print(emptyWord)
    while i < len(wordChoice):  #Following code repeats until i equals the number of letters in the chosen word
        print()
        print("You have",(remainingGuesses),"guesses remaining")
        guesses = input("Guess a letter: ").upper()
        if (guesses) in previousGuesses:
            guesses = print("You have already guessed that letter")

        elif (guesses) in wordChoice:
            letterOccurance = wordChoice.count((guesses))   #Checks the number of elements in the chosen word
            indexOfGuesses = wordChoice.index((guesses))    #Checks the position of elements in the chosen word

            if letterOccurance > 1:
                previousGuesses.append((guesses))   #The list 'previousGuesses' is updated to include the players most recent guess
                remainingGuesses = remainingGuesses - 1     #The number of guesses the has is reduced by one
                i = i + 1
                for k in re.finditer((guesses), (wordChoice)):  #Finds every iteration of the players guess in the chosen word
                    emptyWord[(k.start()):(k.start()+1)] = [(guesses)] #The list containing underscores is updated to contain the correctly guessed letters in the appropriate position
                    correctGuess.append((guesses))  #Correctguess list updated with players most recent guess
                print("The letter",(guesses),"appears",(letterOccurance),"times in the word") #Informs the user how many times their guess occurs in the word
                print(emptyWord)
                print("Correctly guessed letters:",(correctGuess))
                print("Incorrectly guessed letters:",(incorrectGuess))

            else:
                print((guesses),"Was found once in the word")
                correctGuess.append((guesses))
                previousGuesses.append((guesses))
                remainingGuesses = remainingGuesses - 1
                i = i + 1
                emptyWord[(indexOfGuesses):(indexOfGuesses+1)] = [(guesses)] #Again list containing underscores is updated
                print(emptyWord)
                print("Correctly guessed letters:",(correctGuess))
                print("Incorrectly guessed letters:",(incorrectGuess))

                
        else:   #If the user incorrectly guesses a letter
            print((guesses),"was not found in the word")
            incorrectGuess.append((guesses))
            previousGuesses.append((guesses))
            remainingGuesses = remainingGuesses - 1
            i = i + 1
            print(emptyWord)
            print("Correctly guessed letters:",(correctGuess))
            print("Incorrectly guessed letters:",(incorrectGuess))
            
        #User can guess every letter in a word and still have guesses remaining if there are multiple occurances of a letter
        #this checks the length of the word they need to guess with the list containing the number of correct guesses. If length is same game ends.
        if len(correctGuess) == len(wordChoice):
            i = len(wordChoice)
    if len(correctGuess) == len(wordChoice):
        print()
        print("Well done! You correctly guessed the word",(wordChoice))
    else:
        print("\nYou guessed", len(correctGuess),"out of the", len(wordChoice),"letters in the word")
        finalGuess = input("You have one remaining guess to get the word:")
        finalGuess = finalGuess.upper()
        if finalGuess == wordChoice:
            print("\nGood guess! The word was in fact",(wordChoice))
        else:
            print("\nUnlucky. The word you were looking for was",(wordChoice))
            
       
def MainMenu():
    print("\nMain Menu: \nA. Numbers\nB. Strings\nC. Games\nX. Exit\n\n")

    #Handling of user input on the main menu
    userInput = input("Please enter an option (A, B, C or X ): ").upper() #assigns a name to users input and converts whatever they type to uppercase

    if userInput == "A":
        print("Please choose a different option")
        MainMenu()                    #If user types A or B they are met with an error message
    elif userInput == "B":
        print("Please choose a different option")
        MainMenu()
                                                
    elif userInput == "C":                          
        hangMan()      #When C is selected the dice procedure is called upon
 
    elif userInput == "X":  #If users type "X" then the program will terminate
        quit()

    else:
        print("Please enter a valid main menu option (A,B,C or X)")
        MainMenu()
MainMenu()      #Main menu is loaded as soon as the program is run


    

    
input()


