a=input("Enter a first number")
b=int(input("Enter a second number"))
c=int(input("Enter a third number"))
if (a>b) and (a>c):
    print(a,"is the largest number")
elif(b>c):
    print(b,"is the largest number")
else:
    print(c,"is the largest number")