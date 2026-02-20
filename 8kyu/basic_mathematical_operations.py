"""
Language: Python
Kata: Basic Mathematical Operations
Kyu: 8
Description: Your task is to create a function that does four basic mathematical operations.
The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
URL: https://www.codewars.com/kata/57356c55867b9b7a60000bd7
"""


# Solution
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    else:
        return f"{operator} is not valid. Please choose a valid operator: + - * / ."
