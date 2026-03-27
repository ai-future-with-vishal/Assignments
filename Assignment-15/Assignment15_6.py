# 6. Write a lambda function using reduce() which accept list of numbers and return the min element.

from functools import reduce

NumList = [10, 20, 12, 13, 24, 22, 21,83]

MinNumber = reduce(lambda A, B : min(A,B),NumList)

print(MinNumber)
