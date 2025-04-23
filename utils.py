def compute_factorial(number) -> str:
    """
    Computes the factorial of a given integer and returns it as a string.

    If the number is negative, returns "undefined" since factorials are not defined 
    for negative integers. Returns "1" for an input of 0, as 0! is defined to be 1.
    """

    factorial: int = 1

    if number < 0:
        return "undefined"
    
    elif number == 0:
        return "1"
    
    else:
        for i in range(1, number + 1):
            factorial *= i

    return str(factorial)

def is_prime(number: int) -> bool:
    """
    Determines whether a given integer is a prime number.

    A prime number is a number greater than 1 that has no positive divisors
    other than 1 and itself.
    """
    if number <= 1:
        return False

    square_root = int(number ** (1/2))

    for i in range(2, square_root + 1):
        if number % i == 0:
            return False
    return True
    
def is_valid(x: str) -> bool:
    """
    Validates whether the input string is a non-empty, valid integer.

    This function checks two conditions:
    1. The input must be convertible to an integer (i.e., a valid digit).
    2. The input must not be an empty string.
    """
    def __is_digit(x: str) -> bool:
        try:
            int(x)
            return True
        except:
            return False

    def __is_empty(x: str) -> bool:
        if x == '':
            return True
        return False
    
    if not __is_digit(x) or __is_empty(x):
        return False
    return True
    