'''
The objective:

Randomly generate funny sidekick names using Python code that conforms to established style guidelines.

The strategy:
* start with two lists, one with first name, other with last
* randomly generate an element from one, then the other
    * print result (in red, that's the point of file=sys.stderr)
* have an option to repeat the process, or exit the program.
'''
import sys
import random

firstNames = ['Bobby', 'Sugar', 'Grog', 'Vlad', 'The', 'Alfred', 'Bop', 'Bad News', 'Baby Oil', 'Chewy']
lastNames = ['Bodankins', 'Strongjaw', 'Wilafred', 'the Impaler', 'Supafly', 'Boomstick', 'Bojangles', 'Wellington', 'Bears'] 

def promptChoice ():
    choice = input('>>> Y to repeat --- N to exit \n')
    
    if choice.lower() == 'y':
        generateName(firstNames, lastNames)
    elif choice.lower() == 'n':
        exit()
    else:
        print('\n Invalid input.')
        promptChoice()


def generateName (firstNames, lastNames):
    fNameIndex = int(random.random() * len(firstNames))
    lNameIndex = int(random.random() * len(lastNames))

    print('\n Your name is: {} {} \n \n Would you like to generate another name?\n'.format(firstNames[fNameIndex], lastNames[lNameIndex]), file=sys.stderr)
    
    promptChoice()
    

generateName(firstNames, lastNames)