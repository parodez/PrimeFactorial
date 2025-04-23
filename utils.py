def compute_factorial(number) -> str:
    """
    
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
    if number <= 1:
        return False

    square_root = int(number ** (1/2))

    for i in range(2, square_root + 1):
        if number % i == 0:
            return False
        return True
    
def is_valid(x: str) -> bool:
    # Checks if x is a digit
    def __is_digit(x: str) -> bool:
        try:
            int(x)
            return True
        except:
            return False

    # Checks if x is empty
    def __is_empty(x: str) -> bool:
        if x == '':
            return True
        return False
    
    if not __is_digit(x) or __is_empty(x):
        return False
    return True
    