'''Load a text file as a list

Args:
-text file name (and dictionary path, if needed)

Exceptions: 
-IOError if filename not found.

Returns:
-A list of all words in a text file in lower case.

Requires-import sys
'''

import sys


def load(file):
    '''Open a text file and return a list of lowercase strings.'''
    try:
        with open(file, encoding='utf-8') as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f'\nError opening {e}. Terminating program.')
        sys.exit(1)
