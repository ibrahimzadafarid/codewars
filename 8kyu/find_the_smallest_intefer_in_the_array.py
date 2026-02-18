"""
Language: Python
Kata: Find the smallest integer in the array
Kyu: 8
Description: Given an array of integers your solution should find the smallest integer.
URL: https://www.codewars.com/kata/55a2d7ebe362935a210000b2
"""


# Solution
def find_smallest_int(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest
