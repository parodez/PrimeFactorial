#Module for functions related to getting the factorial of a number

#Computes the factorial of a number
#Returns a string containing the factorial of a number
def compute_factorial(number) -> str:
    """
    
    """

    #Declaration and initial value of the return value
    factorial: int = 1

    #If number is a negative, returns the string "undefined"
    if number < 0:
        return "undefined"
    
    #If number is 0, returns the string "1"
    #According to mathetmaticians, the factorial of 0 is 1
    #Source: https://www.thoughtco.com/why-does-zero-factorial-equal-one-3126598
    elif number == 0:
        return "1"
    
    else:
        #Computes the factorial by multiplying all the numbers start from 1 to the given number
        for i in range(1, number + 1):
            factorial *= i

    #Returns a string containing an int value of the factorial of the given number
    #Converts it to string for easy output
    return str(factorial)