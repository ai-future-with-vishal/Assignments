# 1. Write a lambda function using map() which accepts list of numbers and returns a list of squares of each numbers.

ListOfSquires = lambda Numbers : list(map(lambda A : A * A, Numbers))

def main():
    Numbers = [10, 12, 14, 13]

    Ret = ListOfSquires(Numbers)
    
    print(Ret)

if __name__ == "__main__":
    main()
