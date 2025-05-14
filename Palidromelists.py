list=[]
n=int(input("Enter the number of elements of list"))
for i in range(0,n):
    g=input("Enter the element")
    list.append(g)
s=list[ : :-1]
if s==list:
    print("Yes it is a palindrome")
else:
    print("No it is not a palindrome")
