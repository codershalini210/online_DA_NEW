# 14 Take a character input.

# If it is lowercase letter, then check if it is
#  vowel or consonant using nested if (no logical operators).
ch = input("enter any character")
if(ch.islower()):
    if(ch=="a"):
        print("Vowel")
    elif(ch=="e"):
        print("Vowel")
    elif(ch=="i"):
        print("Vowel")
    elif(ch=="o"):
        print("Vowel")
    elif(ch=="u"):
        print("Vowel")
    else:
        print("consonent")
else:
    print("char is in upper case")