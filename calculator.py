from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title('Calculator')

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar() # Updating the text displaed by the label to show the new total
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable = self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate = "key", validatecommand = (vcmd, '%P')) # Validate parameter specifies when validation should occur - default value is 'none' meaning that no validation should be done and key will cause the entry to be validated when it's typed

        # Using lambdas to pass functions into the button constructors
        self.add_button = Button(master, text="+", command = lambda: self.update("add")) # Command keyword parameter to specify the function which should handle each button's click events
        self.subtract_button = Button(master, text="-", command = lambda: self.update("subtract"))
        self.time_button = Button(master, text="*", command = lambda: self.update("time"))
        self.divide_button = Button(master, text="/", command = lambda: self.update("division"))
        self.reset_button = Button(master, text="Reset", command = lambda: self.update("reset"))

        # LAYOUT

        # Using grid method allows us to position widget in a more flexible way
        self.label.grid(row = 0, column = 0, sticky = W) # Place each widget in a cell inside a table by specifying a row and a column
        self.total_label.grid(row = 0, column = 4, columnspan = 2, sticky = E) # Aliging widgets by using sticky parameter

        # Example: sticky = W ==> left-aligned horizontally

        self.entry.grid(row = 1, column = 0, columnspan = 5, sticky = W+E) # To make a widget span multiple columns or rows, use the columnspan/rowspan options

        self.add_button.grid(row = 2, column = 0)
        self.subtract_button.grid(row = 2, column = 1)
        self.time_button.grid(row = 2, column = 2)
        self.divide_button.grid(row = 2, column = 3)
        self.reset_button.grid(row = 2, column = 4)

    # Below method checks the contents of the entry field are a valid integer
    def validate(self, new_text): # Contents will only change if the new value is a valid number
        if not new_text: # The filed is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        elif method == "time":
            self.total *= self.entered_number
        elif method == "division":
            self.total /= self.entered_number
        else: # Reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

# Create the root window by initializing Tk instance
root = Tk()
my_gui = Calculator(root)
root.mainloop() # Method on the main window when we want to run application

