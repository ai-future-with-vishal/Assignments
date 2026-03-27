# 6. Write a program which accept one number and display below pattern.
# Input :   5
# Output : *   *   *   *   *
#          *   *   *   *   
#          *   *   *   
#          *   *   
#          *   

def PattenPrinting(Number):
    for i in range(Number):
        for j in range(Number,i,-1):
            print("*", end=" ")
        print()

def main():
    print("Enter Number : ")
    No = int(input())

    PattenPrinting(No)

if __name__ == "__main__":
    main()