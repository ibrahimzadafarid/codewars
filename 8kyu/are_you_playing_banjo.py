"""
Language: Python
Kata: Are You Playing Banjo?
Kyu: 8
Description: Create a function which answers the question "Are you playing banjo?". If your name starts with the letter "R" or lower case "r", you are playing banjo!
URL: https://www.codewars.com/kata/53af2b8861023f1d88000832

"""


# Solution
def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    return name
