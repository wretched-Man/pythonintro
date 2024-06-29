# In this simple project, I am going to create a function 
# that enables us to do standard arithmetic using
# pyautogui.
# The code requires that the Windows calculator
# application be up and running. It ahould be able to
# perform simple arithmetic.

# To start, the program only runs when the calculator is
# visible

import pyautogui
import time

# utility function to to click on the centre of a 
# calculator button
def writecalc(calckey):
    try:
        x, y = pyautogui.locateCenterOnScreen(\
                                    'keys/' + calckey,\
                                        grayscale=True,\
                                        confidence=0.9)
        pyautogui.click(x, y)
    except:
        print('The key,', calckey, ', could not be'\
              ' found on the calculator.')


try:
    # The program exits when the calculator becomes no
    # longer visible
    # We do this by checking for the 'clear' key or any
    # other key in keys folder. This allows for greater
    # versitility since these keys are not resized and
    # can be found even in a resized calculator.
    while pyautogui.locateOnScreen('keys/clear.png',\
                                    grayscale=True,\
                                     confidence=0.9):
        # If the calculator is visible, get user input
        # It is up to the user to ensure that the
        # character input is correct.
        
        user_input = input('What do you want to'\
                           ' calculate? [0 - 9, */-+.]\n')
    
        #remove ws from string
        arithmetic = user_input.replace(' ', '')
        # A dictionary of operators and filename
        ops_dict = {'*': 'multiply.png',
                    '/': 'divide.png',
                    '-': 'subtract.png',
                    '+': 'addition.png',
                    '.': 'decimal.png'}
        
        # For the numbers 0 - 9, we will do automatically,
        # like so:
        for op in range(len(arithmetic)):
            value = ops_dict.get(arithmetic[op])

            #search for it in ops_dict
            if value is not None:
                #if found 
                writecalc(value)
            else:
                #check if it is between 0-9
                numeric = ord(arithmetic[op]) - 48

                if numeric in range(0, 10):
                    writecalc(str(numeric)+'.png')
                else:
                    #it is not a numeral or an operator
                    # its image will not exist
                    raise pyautogui.ImageNotFoundException
                
        # By this point, we have already written the
        # whole expression we press the equal sign to
        # get the answer
        writecalc('equal.png')

        # wait 10 secs
        time.sleep(3)

        #clear output
        writecalc('clear.png')
except pyautogui.ImageNotFoundException:
    print("Can't see. Terminated.")
