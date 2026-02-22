"""
Language: Python
Kata: A Needle in the Haystack
Kyu: 8
Description: Can you find the needle in the haystack? Write a function findNeedle() that takes an array full of junk but containing one "needle" After your function finds the needle it should return a message (as a string) that says: "found the needle at position " plus the index it found the needle
URL: https://www.codewars.com/kata/56676e8fabd2d1ff3000000c

"""


# Solution
def find_needle(hackstack):
    return f"found the needle at position {hackstack.index('needle')}"


# Solution 2


def find_needle_two(hackstack):
    for i in range(len(hackstack)):
        if hackstack[i] == "needle":
            return f"found the needle in position {i}"
