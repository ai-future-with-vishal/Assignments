# 5. Write a program which accepts one number and prints all number till that number.
# Input : 10
# Output : 1 3 5 7 9

def OddNumbers():
    print("Enter number : ")
    No = int(input())

    for i in range(No+1):
        if (i % 2 == 1):
            print(i)

OddNumbers()
