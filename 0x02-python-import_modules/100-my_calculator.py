#!/usr/bin/python3
from calculator_1 import *

def main():
    try:
        a, operator, b = input().split()
        a = int(a)
        b = int(b)

        if operator == "+":
            print(f"{a} + {b} = {add(a, b)}")
        elif operator == "-":
            print(f"{a} - {b} = {subtract(a, b)}")
        elif operator == "*":
            print(f"{a} * {b} = {multiply(a, b)}")
        elif operator == "/":
            print(f"{a} / {b} = {divide(a, b)}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")

if __name__ == "__main__":
    main()
