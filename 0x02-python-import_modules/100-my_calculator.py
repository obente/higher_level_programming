#!/usr/bin/python3
def main():
    from calculator_1 import add, div, mul, sub
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        print(add(a, b))

    elif argv[2] == '-':
        print(sub(a, b))

    elif argv[2] == '*':
        print(mul(a, b))

    elif argv[2] == '/':
        print(div(a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
