"""
Language: Python
Kata: Counting sheep...
Kyu: 8
Description: Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
URL: https://www.codewars.com/kata/54edbc7200b811e956000556
"""


# Solution
def count_sheep(sheep):
    total = 0
    for sh in sheep:
        if sh:
            total += 1
    return total
