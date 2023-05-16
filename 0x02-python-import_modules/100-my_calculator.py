#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, b = int(argv[1]), int(argv[3])
    math_symbols = ['+', '-', '*', '/']

    if argv[2] not in math_symbols:
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)

    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    operator = argv[2]
    result = operators[operator](a, b)

    print("{:d} {} {:d} = {:d}".format(a, operator, b, result))

