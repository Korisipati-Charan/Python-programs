n=int(input("Enter rhe number"))
org=n
r=0
while n>0:
    dig=n%10
    r=r*10+dig
    n=n//10
if r==org:
    print("yes it is a palindrome")
else:
    print("no it is not a palindrome")
