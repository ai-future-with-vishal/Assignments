# 2. Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is Even then it shoud Display "Even Number" otherwise Display "Odd Number" on console.
# Input : 11                Output : "Odd Number"
# Input : 8                 Output : "Even Number"

def ChkNum(Number):
    if(Number % 2 == 0):
        return True
    else:
        return False
    
def main():
    print("Enter number : ")
    No = int(input())

    Result = ChkNum(No)

    if(Result == True):
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()
