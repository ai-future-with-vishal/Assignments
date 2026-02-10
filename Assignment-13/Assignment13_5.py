# 5. Write a program which accepts Marks and displays grads.
# Condition Example : 
# >= 75 - Distinction
# >= 60 - First Class
# >= 50 - Second Class
# < 50 - Fail

def Grade():
    print("Enter Marks : ")
    Marks = int(input())

    if(Marks >= 75):
        print("distinction")
    elif(Marks >= 60):
        print("First Class")
    elif(Marks >= 50):
        print("Second Class")
    else:
        print("Fail")

Grade()