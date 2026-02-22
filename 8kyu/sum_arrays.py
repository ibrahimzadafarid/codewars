"""
Language: Python
Kata: Sum Arrays
Kyu: 8
Description: Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative. If the array is empty, return 0.
URL: https://www.codewars.com/kata/53dc54212259ed3d4f00071c

"""


# Solution
def sum_array(a):
    total = 0
    for num in a:
        total += num
    return total


# Solution 2


def sum_array2(a):
    return sum(a)
