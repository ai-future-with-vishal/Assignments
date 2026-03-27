# 7. Write a program which accept one number and display below pattern.
# Input : 5
# Output : 1    2   3   4   5
#          1    2   3   4   5
#          1    2   3   4   5
#          1    2   3   4   5
#          1    2   3   4   5

def PatternPrinting(Number):
    for i in range(1,Number+1):
        for j in range(1,Number+1):
            print(j, end=" ")
        print()

def main():
    print("Enter number : ")
    No = int(input())

    PatternPrinting(No)

if __name__ == "__main__":
    main()