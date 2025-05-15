# Assignment2_1.py

import Arithmetic

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", Arithmetic.Add(a, b))
    print("Subtraction:", Arithmetic.Sub(a, b))
    print("Multiplication:", Arithmetic.Mult(a, b))
    print("Division:", Arithmetic.Div(a, b))

if __name__ == "__main__":
    main()
