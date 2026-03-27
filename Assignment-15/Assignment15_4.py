# 4. Write a lambda function using reduce() which accepts list of numbers and returns the addition of all element.

from functools import reduce


NumList = [10, 20, 12, 13, 24, 22, 21,83]

ListofAddition = reduce(lambda A, B : A + B, NumList)

print(ListofAddition)
    