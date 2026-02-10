# 9. Write a program which displays first 10 even numbers on screen.
# Output : 2    4   6   8   10  12  14  16  18 20

def EvenNumber():
    Count = 0
    i = 1
    while True:
        if(i % 2 == 0):
            print(i)
            Count = Count + 1
        
        if(Count == 10):
            break
        i = i + 1

def main():
    EvenNumber()

if __name__ == "__main__":
    main()