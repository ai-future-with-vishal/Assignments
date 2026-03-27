# 10. Write a lambda function using filter() which accepts a list of numbers and returns count of even number.

from itertools import count


NumList = [10, 20, 15, 30, 12, 13, 24, 22, 21,83]

CountOfEven = len(list(filter(lambda A : A % 2 == 0, NumList)))

print(CountOfEven)
