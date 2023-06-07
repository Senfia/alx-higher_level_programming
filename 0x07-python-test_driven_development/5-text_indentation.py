#!/usr/bin/python3
"""
This is the "text_indentation" module.

Adds two new lines after a set of characters.
"""


def text_indentation(text):
    """Prints text with added two newlines after each characters: ., ? and :.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    exact = 0
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print("{:s}".format(i), end="")
            print()
            print()
            exact = 1
        else:
            if not exact:
                print("{:s}".format(i), end="")
            else:
                if i == ' ' or i == '\t':
                    continue
                print("{:s}".format(i), end="")
                exact = 0
