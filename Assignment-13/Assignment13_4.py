# 4. Write a Program which accept one number and prints binary equivalent.

def BinaryEquivalent(Number):
    if(Number == 0):
        return "0"
    
    Binary_str = ""
    while Number > 0:
        rem = Number % 2
        Binary_str = str(rem) + Binary_str
        Number //= 2
    
    return Binary_str

def main():
    print("Enter Number : ")
    No = int(input())

    Ret = BinaryEquivalent(No)

    print(Ret)
if __name__ == "__main__":
    main()