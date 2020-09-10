#Regan_Matthew-CA03
#10/2017
#Outputting a pyramid of numbers


def Numbers():
    userInteger = int(input("Please enter an integer: "))
    if userInteger < 1 or userInteger > 27:
        print("Please enter an integer in the range of 1 to 27")    #if user integer doesn't fall within specified range they will be given this error message

    else:
        print("Your chosen number is:",userInteger) #prints integer the user input
        for i in range (0,userInteger+1):
            print(i * ("%s " %(i)))     #the value of 'i' is printed the same number of times as its value. A space is inserted between each number also
            for j in range (0, userInteger):
                print(end=" ")          #A space is inserted for every column to the range of the userInteger
            userInteger = userInteger - 1


def Main():
    print("\nMain Menu: \nA. Numbers\nB. Strings\nC. Games\nX. Exit\n\n")

    userInput = input("Please enter an option (A, B, C or X ): ").upper()

    if userInput == "A":
        Numbers()       #If userInput matches exactly "A" then Numbers module is called upon
        
    elif userInput == "B":
        print("Please choose a different option")
        Main()
                                                    
    elif userInput == "C":                          #If user types B or C they are met with an error message
        print("Please choose a different option")
        Main()

    elif userInput == "X":  #If users type "X" then the program will terminate
        quit()
Main()      #Main menu is loaded as soon as the program is run


input()

#http://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/  SOURCE FOR PYRAMID SHAPE
