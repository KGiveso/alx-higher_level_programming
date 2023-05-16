#!/usr/bin/python3
import calculator_1

def main():
    a, operator, b = input().split()

    if len(a) == 0 or len(operator) == 0 or len(b) == 0:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(a)
    b = int(b)

    if operator == "+":
        result = calculator_1.add(a, b)
    elif operator == "-":
        result = calculator_1.subtract(a, b)
    elif operator == "*":
        result = calculator_1.multiply(a, b)
    elif operator == "/":
        result = calculator_1.divide(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print(f"{a} {operator} {b} = {result}")

if __name__ == "__main__":
    main()
