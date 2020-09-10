#Regan_Matthew-CA06
#11/2017
#Morse code interpreter which de-cyphers set expressions in morse. Also compiles and sorts dictionary alphabetically

morseBookOriginal = {
"B":"-...", "C":"-.-.", "G":"'--.",
"H":"....", "D":"-..",  "F":"..-.",
"M":"--",   "N":"-.",   "J":".---",
"K":"-.-",  "L":".-..", "P":".--.",
"Q":"--.-", "R":".-.",  "V":"...-",
"W":".--",  "X":"-..-", "S":"...",
"T":"-",    "Y":"-.--", "Z":"--.."}     #Initial un-ordered Morse dictionary

morseVowels = {"A":".-", "E":".", "I":"..", "O":"---", "U":"..-"}   #Dictionary containing vowels

def morseInterpretation():

# TASK A) Compiling unordered morseBook with vowel dictionary
    morseBookLookup = {}    #Creating an empty dictionary where the original morseBook and the vowels are added to.
    for key, value in  morseBookOriginal.items():
         morseBookLookup[value] = key   #All keys and associated values are added to the new dictionary
    for key, value in  morseVowels.items():
         morseBookLookup[value] = key
         

# TASK B) Translating coded message into english
    codedMessage = [".--","....","-.--", ".-..","-.--","-.","-..-", "-.-.",".-.","-.--"] #"Why Lynx Cry"
    print("\nThe researchers message was:\n", codedMessage)
    decodedMessage = "";
    for key in codedMessage:
            decodedMessage += morseBookLookup[key]  #Finds the keys associated to the 'values' in the coded message    
    print("Decoded message:", decodedMessage)

    
# TASK C) Unordered alphabet without vowels
    print("\nThe un-ordered alphabet and their morse code equivalent(not containing vowels):")
    for key, value in morseBookOriginal.items():
        print (key, value)

        
# TASK D) Alphabetical Morse Code book with vowels
    print("\nThe alphabet and their morse code equivalant:")
    for key, value in  sorted(morseBookLookup.items(), key=lambda x: x[1]): #Using lambda to sort the dictionary by the value of the keys(1) in this case the letters in the alphabet
        print (value , key)



def MainMenu():
    print("\nMain Menu: \nA. Numbers\nB. Strings\nC. Games\nX. Exit\n\n")

    #Handling of user input on the main menu
    userInput = input("Please enter an option (A, B, C or X ): ").upper()

    if userInput == "A":
        print("Please choose a different option")
        MainMenu()                    #If user types A or C they are met with an error message
    elif userInput == "B":
        morseInterpretation()   #When B is selected the morse procedure is called upon
                                                
    elif userInput == "C":
        print("Please choose a different option")
        MainMenu()      
 
    elif userInput == "X":  #If users type "X" then the program will terminate
        quit()

    else:
        print("Please enter a valid main menu option (A,B,C or X)")
        MainMenu()
MainMenu()      #Main menu is loaded as soon as the program is run

input()
