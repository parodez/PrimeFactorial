#Module for functions related to determining if a number is prime

#Checks if a number is a prime number
def is_prime(number: int) -> bool:
    #If number is negative, the number is not a prime, returning the string False
    if number <= 1:
        return False

    #Gets the square root of the number
    square_root = int(number ** (1/2))

    #Checks all the numbers from 2 to square_root
    #Returns False if any number is divisible by the number
    for i in range(2, square_root + 1):
        if number % i == 0:
            return False
    
    #Returns True since the number is not divisible by any number except 1 and itself
    return True