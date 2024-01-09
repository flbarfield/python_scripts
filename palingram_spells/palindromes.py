'''
Load digital dictionary file as a list of words
Create an empty list to hold palindromes
Loop through each word in a word list:
    if word is the same as word sliced backwards:
        append word to palindrome list
Print Palindrome List
'''

import load_dictionary

dict_sample = load_dictionary.load('./2of12.txt')

def return_palindromes(word_list):
    '''recieves a word list, and tests words within.
    returns a list of words that are palindromes.
    '''

    pali_list = []

    for word in word_list:
        if word == word[::-1] and len(word) > 1:
            pali_list.append(word)
    return pali_list

print(return_palindromes(dict_sample))
