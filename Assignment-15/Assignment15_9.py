# 9. Write a lambda function using reduce() which accepts a list of numbers and returns product of all element.

from functools import reduce

NumList = [10, 20, 15, 30, 12, 13, 24, 22, 21,83]

ProductOfElement = reduce(lambda A, B : A * B, NumList)

print(ProductOfElement)
