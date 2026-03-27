# Write a lambda function using filter() which accept a list of strings and return a list of strings having length greater than 5.

ListOFStrings = ["Vishal", "Ganesh", "Dhande", "Marvellous", "Hello", "Hi", "Chai"]

FilteredStrings = list(filter(lambda A : len(A) > 5 ,ListOFStrings))

print(FilteredStrings)