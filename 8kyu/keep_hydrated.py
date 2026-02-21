"""
Language: Python
Kata: Keep Hydrated
Kyu: 8
Description: Nathan loves cycling.
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.
URL: https://www.codewars.com/kata/582cb0224e56e068d800003c
"""


# Solution
def litres(time):
    return int(time * 0.5)
