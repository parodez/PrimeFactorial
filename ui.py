from tkinter import *
from utils import utils as ut

class display(Tk):
    """
    A Tkinter-based GUI class for checking prime numbers and computing factorials.

    This class sets up the main application window with a fixed grid layout and
    custom-styled widgets, including labels, an entry field, and a button. It uses
    an internal method to configure widgets and encapsulates user interaction logic
    through a button-click handler.

    Attributes are initialized using a widget configuration method, allowing for
    organized access and modular design.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the PrimeFactorial GUI window.

        Sets up the main application window with a fixed size, background color,
        and grid layout. Configures row and column weights for responsive design.
        Adds visual grid borders using label widgets, and disables window resizing.

        Initializes and stores widget components including labels, entry field, and button
        by calling the internal widget configuration method.
        """
        super().__init__(*args, **kwargs)
        
        self.title('PrimeFactorial')
        self.geometry('400x400')

        self.grid_propagate(False)

        for x in range(10):
            Grid.columnconfigure(self, x, weight=1, uniform='row')
            Label(self, width = 1, bg = '#F5EEDD').grid(row = 0, column = x, sticky = N+S+E+W)
        for y in range(10):
            Grid.rowconfigure(self, y, weight=1, uniform='row')
            Label(self, width = 1, bg = '#F5EEDD').grid(row = y, column = 0, sticky = N+S+E+W)

        self.configure(background='#F5EEDD')
        self.resizable(False, False)

        self.__configurations = self.__widget_configurations()

        # Labels
        self.label = self.__configurations['label']
        self.label_error = self.__configurations['label_error']
        self.label_prime = self.__configurations['label_prime']
        self.label_factorial = self.__configurations['label_factorial']

        # Entry
        self.entry_number = self.__configurations['entry_number']
        
        # Button
        self.button = self.__configurations['button']

    def __widget_configurations(self) -> dict:
        """
        Creates and configures all the widgets used in the PrimeFactorial GUI.

        This method initializes labels, an entry field, and a button with specified
        styles, colors, fonts, and placements using the Tkinter grid layout. It 
        returns a dictionary containing references to each widget so they can be 
        accessed and managed elsewhere in the class.
        """
        color1: str = '#F5EEDD'
        color2: str = '#7AE2CF'
        color3: str = '#077A7D'
        color4: str = '#06202B'

        # Label configurations

        # label
        label: Label = Label(self, text = "Enter Number:", font = ('Arial', 16),
                      width = 1, height = 1, fg = '#000000', bg = color1)
        label.grid(row = 1, column = 3, columnspan = 4, rowspan = 1, sticky = N+S+E+W)

        # label_error
        label_error: Label = Label(self, text = "", font = ('Arial', 10), width = 1,
                                   height = 1, fg = '#FF0000', bg = color1)
        label_error.grid(row = 0, column = 2, columnspan = 6, rowspan = 1, sticky = N+S+E+W)
        
        # label_prime
        label_prime: Label = Label(self, text = "", font = ('Arial', 10), width = 1,
                                   height = 1, fg = color1, bg = color3)
        label_prime.grid(row = 4, column = 1, columnspan = 8, rowspan = 2, sticky = N+S+E+W)
      
        # label_factorial
        label_factorial: Label = Label(self, text = "", font = ('Arial', 10), width = 1,
                                       height = 1, fg = color1, bg = color4,
                                       wraplength = 275)
        label_factorial.grid(row = 6, column = 1, columnspan = 8, rowspan = 3, sticky = N+S+E+W)

        # Entry configurations
        entry_number = Entry(self, width = 1, bg = '#FFFFFF', font = ('Arial', 16),
                             justify = 'center')
        entry_number.grid(row = 2, column = 1, columnspan = 8, rowspan = 1, sticky = N+S+E+W)
        entry_number.insert(0, "")

        # Button configurations
        button: Button = Button(self, text = "Enter", font = ('Arial', 16), width = 1,
                                height = 1, fg = '#000000', 
                                command = self.clicked,
                                bg = color2)
        button.grid(row = 3, column = 4, columnspan = 2, rowspan = 1, sticky = N+S+E+W)
        
        # Configurations dictionary
        configurations: dict = {
            'label': label,
            'label_error': label_error,
            'label_prime': label_prime,
            'label_factorial': label_factorial,
            'entry_number': entry_number,
            'button': button,
        }

        return configurations
        
    def clicked(self):
        """
        Handles the logic executed when the 'Enter' button is clicked.

        Validates the input from the entry field to ensure it is a non-empty,
        numeric value. If the input is invalid, displays an error message in the
        designated error label.

        This method relies on utility functions from the `utils` module for input
        validation, prime checking, and factorial computation.
        """
        user_input = ut(self.entry_number.get())

        if not user_input.is_valid():
            self.label_error.config(text = "Please input a valid value.")
            self.label_prime.config(text = "")
            self.label_factorial.config(text = "")

        else:
            self.label_error.config(text = '')

            str_number: str = self.entry_number.get()
            int_number: int = int(str_number)

            if user_input.is_prime():
                self.label_prime.config(text = f" {int_number} is a prime number.")
            else:
                self.label_prime.config(text = f" {int_number} is not a prime number.")
            
            self.label_factorial.config(text = f"The factorial of {int_number} is:\n{user_input.compute_factorial()}.")

        self.entry_number.delete(0, END)