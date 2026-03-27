# 2. Write a lambda function which accepts list of numbers and prints list of even numbers.

Number = [10, 20, 30, 27, 25]

EvenNumberList = list(filter(lambda A : A % 2 == 0, Number))
                      
print(EvenNumberList)