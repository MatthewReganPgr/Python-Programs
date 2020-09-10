#10/2017
#Password validation

import re


#else:
#    print ("Password is not between 8 and 15 characters or does not contain a mixture of numbers and characters")

def GetPassword():
    while True:
      password = input("Please enter a password: ")
      if PasswordIsValid(password):
          break
    return password

def PasswordIsValid(password):
    length = len(password)

    if(IsAlphNumeric(password) == False):
        print("Password must contain a number")
        return False
    
    if(length < 8):
       print("Password is too short")
       return False;

    if(length > 15):
       print("Password is too long")
       return False;

    if(HasNumber(password) == False):
        print("Password must contain a number")
        return False

    if(HasChar(password) == False):
        print("Password must contain a character")
        return False

    return True

def IsAlphNumeric(password):
    return re.match("^[A-Za-z0-9]*$", password)

def HasNumber(password):
    return any(char.isdigit() for char in password)

def HasChar(password):
  return any( re.match("^[A-Za-z]*$", char) for char in password)


def Main():
    userPassword = GetPassword()
    print (userPassword)

  

Main()

input()
