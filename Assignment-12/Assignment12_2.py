# 2. Write a program which accepts one number and prints its factors.
# Input : 12
# Output : 1 2 3 4 6 12

def Factor(Number):
    for i in range(1,Number+1):
        if(Number % i == 0):
            print(i)


def main():
    print("Enter number : ")
    No = int(input())

    Factor(No)

if __name__ == "__main__":
    main()
