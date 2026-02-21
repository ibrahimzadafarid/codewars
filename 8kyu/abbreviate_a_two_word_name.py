"""
Language: Python
Kata: Abbreviate a Two Word Name
Kyu: 8
Description: Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
URL: https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
"""


# Solution
def abbrev_name(name):
    first, last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"
