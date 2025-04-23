#Module for functions related to validating user input

#Checks if an input is a digit
#Returns True if digit, False otherwise
def is_digit(x: str) -> bool:
    try:
        int(x)
        return True
    except:
        return False

#Checks if an input is empty
#Returns True if empty, False otherwise 
def is_empty(x: str) -> bool:
    if x == '':
        return True
    return False