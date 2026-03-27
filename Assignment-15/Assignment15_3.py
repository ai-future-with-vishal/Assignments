# 3. Write a lambda function using filter() which accepts list of numbers and returns a list of odd numbers.

Numbers = [10, 20, 23, 21, 24, 28, 34, 11]

OddNumberList = list(filter(lambda A : A % 2 == 1, Numbers))

print(OddNumberList)