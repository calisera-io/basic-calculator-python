# Basic Calculator in Python

import sys

def getInput(msg, cast = 'str'):
    while True:
        try:
            value = input(msg+" ")
            value = value.strip()
            match cast:
                case 'int':
                    value = int(value)
                case 'float':
                    value = float(value)
                case 'str':
                    pass
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
    print("Hit Ctrl-C to quit")

    # Get user input
    num1 = getInput("Enter first number:", 'float')
    op = getInput("Enter operator (+, -, *, /):")
    num2 = getInput("Enter second number:", 'float')

    # Perform calculation
    match op:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2:
                result = num1 / num2
            else:
                return "Error! Division by zero."
        case _:
            return "Invalid operator!"

    return f"Result: {result}"

# Run calculator
while True:
    print(calculator())
