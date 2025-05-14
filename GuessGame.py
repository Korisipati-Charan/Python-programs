import random
target=random.randint(1,100)
print("computer has chosen a number.Take a guess to find it")
while True:
    s=input("Enter the guess or quit(Q)")
    if (s=="Q"):
        print("Quitting..")
        break
    else:
        s=int(s)
    if (target==s):
        print("correct guess")
        break
    if (target<s):
        print("The number is too big")
    if (target>s):
        print("The number is too small")
print("---GAME OVER---")
