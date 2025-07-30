# Basic Calculator in Python

import sys

def getInput(msg, cast = 'str'):
    while True:
        try:
            value = input(msg+" ")
            match cast:
                case 'int':
                    value = int(value)
                case 'float':
                    value = float(value)
                case 'str':
                    value = str(value).rstrip()
                case _:
                    raise ValueError('Unkown cast.')
            break
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("Invalid input. Try again.")
    return value


def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    # Get user input
    num1 = getInput("Enter first number:", 'float')
    op = getInput("Enter operator (+, -, *, /):")
    num2 = getInput("Enter second number:", 'float')

    # Perform calculation
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator!"

    return f"Result: {result}"

# Run calculator
print(calculator())
