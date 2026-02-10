# 10. Write a program which accept name from user and Display length of that name.
# Input : Marvellous            Output : 10

def LengthOfCharactor(Name):
    print(len(Name))

def main():
    print("Enter name : ")
    Val = input()

    LengthOfCharactor(Val)

if __name__ == "__main__":
    main()
