"""
Language: Python
Kata: Convert number to reversed array of digits
Kyu: 8
Description: Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
URL: https://www.codewars.com/kata/5583090cbe83f4fd8c000051

"""


# Solution
def digitize(n):
    digits = []
    for d in str(n):
        digits.insert(0, int(d))
    return digits
