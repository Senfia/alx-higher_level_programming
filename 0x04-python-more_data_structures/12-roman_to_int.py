#!/usr/bin/python3
def roman_to_int(roman_string):
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    final = 0
    for r in reversed(roman_string):
        final += numbers.get(r, 0) if final < numbers[r] * 5 else -numbers[r]
    return (final)
