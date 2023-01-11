#!/usr/bin/python3
""" This module prints a text with 2 new lines after each
of these characters '. ? and :
"""


def text_indentation(text):
    """ This function prints a text with 2 new lines after
    each of these characters '.?:'
    """
    # --- checking if not string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # ____ if it is, loop through
    for i in range(len(text)):
        # - - check if it's the first element
        if (i == 0 and text[i] == ' '):
            continue
        if (i == (len(text) - 1) and text[i] == ' '):
            break
        # - - if it's not in character
        print(text[i], end='')
        # - - - check if character is met, print 2 newlines
        if (text[i] in ['.', '?', ':']):
            print("\n\n", end='')
