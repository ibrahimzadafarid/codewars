"""
Language: Python
Kata: Century From Year
Kyu: 8
Description: The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc. Given a year, return the century it is in.
URL: https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097
"""

# Solution


def century(year):
    return (year - 1) // 100 + 1
