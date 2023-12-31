'''Write a script that takes in a string as an input and returns
a barchart display

Basically means that given a string, I'll need to seperate 
each character and show how many times they appear within the string
by repeating the character as a value for the key

ex:
alabama
a: ['a', 'a', 'a', 'a',]
(and so on for all the other letters in alabama)

Steps:

* create dict with all letters of the alphabet as keys, values with
    empty lists
* trim white space / split string / loop through string
    * for letter in string:
        * push letter into the value of corresponding key
* display dictionary to user
'''

def bar_chart_start ():
    '''script init''' 
    bar_chart = {
        'a': [], 'b': [], 'c': [], 'd': [],
        'e': [], 'f': [], 'g': [], 'h': [],
        'i': [], 'j': [], 'k': [], 'l': [],
        'm': [], 'n': [], 'o': [], 'p': [],
        'q': [], 'r': [], 's': [], 't': [],
        'u': [], 'v': [], 'w': [], 'x': [],
        'y': [], 'z': []
    }

    state = True
    user_string = input('Please input a phrase. \n >>> ').lower().strip()
    for letter in user_string:
        if letter in bar_chart:
            bar_chart[letter].append(letter)
    print(bar_chart)

    while state is True:
        choice = input('Would you like to enter another phrase? \n \
                    y for Yes, n for No \n >>> ' ).lower().strip()

        if choice == 'y':
            bar_chart_start()
        elif choice == 'n':
            state = False
        else:
            print('Invalid Entry. Please try again.')

bar_chart_start()
