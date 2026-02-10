# 5. Write a program which display 10 to 1 on screen.
# Input : 10
# Output : 10   9    8   7   6   5   4   3   2   1

def ReverseNumber():
    i = 10
    while i >= 1:
        print(i)
        i = i - 1

def main():
    ReverseNumber()

if __name__ == "__main__":
    main()