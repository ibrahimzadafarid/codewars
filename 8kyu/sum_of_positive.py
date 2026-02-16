"""
Language: Python
Kata: Sum of positive
Kyu: 8
Description: You get an array of numbers, return the sum of all of the positives ones.
URL: https://www.codewars.com/kata/5715eaedb436cf5606000381
"""

# Solution

def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total
