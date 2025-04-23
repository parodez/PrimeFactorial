class utils:
    def __init__(self):
        self.str_user_input: str = ''
        self.int_user_input: int = 0
        pass

    def compute_factorial(self) -> str:
        """
        Computes the factorial of a given integer and returns it as a string.

        If the number is negative, returns "undefined" since factorials are not defined 
        for negative integers. Returns "1" for an input of 0, as 0! is defined to be 1.
        """

        result: int = 1

        if self.int_user_input < 0:
            return "undefined"
        
        elif self.int_user_input == 0:
            return "1"
        
        else:
            for i in range(1, self.int_user_input + 1):
                factorial *= i

        return str(result)

    def is_prime(self) -> bool:
        """
        Determines whether a given integer is a prime number.

        A prime number is a number greater than 1 that has no positive divisors
        other than 1 and itself.
        """
        if self.int_user_input <= 1:
            return False

        square_root = int(self.int_user_input ** (1/2))

        for i in range(2, square_root + 1):
            if self.int_user_input % i == 0:
                return False
        return True
        
    def is_valid(self) -> bool:
        """
        Validates whether the input string is a non-empty, valid integer.
        """
        if not self.__is_digit(self.str_user_input) or self.__is_empty(self.str_user_input):
            return False
        return True
    
    def __is_digit(self) -> bool:
        try:
            int(self.str_user_input)
            return True
        except:
            return False

    def __is_empty(self) -> bool:
        if self.str_user_input == '':
            return True
        return False 
        
    