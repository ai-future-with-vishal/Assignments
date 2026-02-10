# 1. Write a program which accepts one Character and checks whether it is Vowel or Consonant.
# Input : a
# Output : Vowel

def VowelorConsonant():
    print("Enter Character : ")
    Char = chr(input())

    if ((Char == "a","e","i","o","u") or (Char == "A","E","O","I","U")):
        print("Vowel")
    else:
        print("Consonent")

VowelorConsonant()