import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    question = simpledialog.messagebox(title='The magic 8 ball ',prompt='ask the 8 ball a question')
    # Make a variable and initialize it to a random number between 0 and 3
    a = random.randint(0,3)
    # If the random number is 0
    if a == 0:

        # tell the user "Yes"

    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
