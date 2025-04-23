from prime import is_prime
from factorial import compute_factorial
from validate import is_digit, is_empty
from tkinter import *
from tkinter import messagebox

#Class for the UI window
class display(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('PrimeFactorial')
        self.geometry('400x400')
        self.grid_propagate(False)
        for x in range(10):
            Grid.columnconfigure(self, x, weight=1, uniform='row')
            Label(self, width = 1, bg = '#FFDBDB').grid(row = 0, column = x, sticky = N+S+E+W)
        for y in range(10):
            Grid.rowconfigure(self, y, weight=1, uniform='row')
            Label(self, width = 1, bg = '#FFDBDB').grid(row = y, column = 0, sticky = N+S+E+W)
        self.configure(background='#FFDBDB')
        self.resizable(False, False)

        self.__configurations = self.__widget_configurations()

        # Labels
        self.label = self.__configurations['label']
        self.label_prime = self.__configurations['label_prime']
        self.label_factorial = self.__configurations['label_factorial']

        # Entry
        self.entry_number = self.__configurations['entry_number']
        
        # Button
        self.button = self.__configurations['button']

    def __widget_configurations(self) -> dict:
        # Label configurations
        label: Label = Label(self, text = "Enter Number:", font = ('Arial', 16),
                      width = 1, height = 1, fg = '#000000', bg = '#FFDBDB')
        label.grid(row = 1, column = 3, columnspan = 4, rowspan = 1, sticky = N+S+E+W)
        
        label_prime: Label = Label(self, text = "", font = ('Arial', 10), width = 1,
                                   height = 1, fg = '#FFDBDB', bg = '#644A07')
        label_prime.grid(row = 4, column = 1, columnspan = 8, rowspan = 2, sticky = N+S+E+W)
      
        label_factorial: Label = Label(self, text = "", font = ('Arial', 10), width = 1,
                                       height = 1, fg = '#FFC6C6', bg = '#594100',
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
                                command = lambda: clicked(self.label_prime, self.label_factorial, self.entry_number),
                                bg = '#FFC6C6')
        button.grid(row = 3, column = 4, columnspan = 2, rowspan = 1, sticky = N+S+E+W)
        
        # Configurations dictionary
        configurations: dict = {
            'label': label,
            'label_prime': label_prime,
            'label_factorial': label_factorial,
            'entry_number': entry_number,
            'button': button,
        }

        return configurations
        



#Is called when button is clicked
#Takes control of label_prime, label_factorial, and entry_number
def clicked(label_prime: Label, label_factorial: Label, entry_number: Entry):
    #Checks if value in entry_number is empty or not a digit
    #Shows a messagebox if either is true
    if is_empty(entry_number.get()) or not is_digit(entry_number.get()):
        messagebox.showinfo(message = "Please input a valid value.")

    else:
        #Stores processed variables for easy access and readability
        str_number: str = entry_number.get()
        int_number: int = int(str_number)
        
        #Checks if int_number is prime
        if is_prime(int_number):
            label_prime.config(text = str_number + f" {int_number}is a prime number.")
        else:
            label_prime.config(text = str_number + " is not a prime number.")
        
        #Comutes the factorial of the number
        label_factorial.config(text = "The factorial of " + str_number + " is:\n" + compute_factorial(int_number) + ".")

        #Resets the value in entry_number
        entry_number.delete(0, END)

if __name__ == "__main__":
    window = display()
    window.mainloop()
