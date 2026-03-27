# 5. Write a lambda function using reduce() which accepts a list of numbers and returns a maximum element.

from functools import reduce


NumList = [10, 20, 12, 13, 24, 22, 21,83]

MaxNum = reduce(lambda A ,B : max(A,B),NumList)

print(MaxNum)