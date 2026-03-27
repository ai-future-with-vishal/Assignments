# 8. Write a lambda function using filter() which accepts a list of numbers and returns list of numbers divisible by both 3 and 5.

NumList = [10, 20, 15, 30, 12, 13, 24, 22, 21,83]

NewList = list(filter(lambda A : A % 3 == 0 and A % 5 == 0, NumList))

print(NewList)