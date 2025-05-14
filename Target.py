list=[]
list2=[]
a=int(input("Enter the length of array"))
g=int(input("Enter the target value"))
for i in range(0,a):
    num=int(input("Enter the number you want to enter into the array"))
    list.append(num)
for i in range(0,a):
    n1=list[i]
    for j in range(0,a):
        n2=list[j]
        target=n1+n2
        if target==g:
            list2.append(n1)
            list2.append(n2)
print(list2)
print("After removing similar elements")
list3=set(list2)
print(list3)
