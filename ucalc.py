import uart
import math

print(uart.logo_Calc)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def power(n1, n2):
    return math.pow(n1, n2)


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**':power
}


def calculator():
    num1 = float(input("What's the first number? : "))

    for i in operations:
        print(i)
    should_continue = False
    while not should_continue:
        operation_symbol = input("Which operation you want to perform? : ")
        num2 = float(input("What's the next number? : "))

        calculation_functions = operations[operation_symbol]
        answer = calculation_functions(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        result = input(f"Type 'y' to continue with {answer}, or type 'n' to exit : ")

        if result == "y":
            num1 = answer
        else:
            should_continue = True
            calculator()

calculator()
