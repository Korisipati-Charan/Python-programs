e=input("Enter something")
dict={}
for i in range(0,len(e)):
    left=i
    right=i
    while left >= 0 and right < len(e) and e[left] == e[right]:
        dict[i]=e[left:right+1]
        left=left-1
        right=right+1
print(dict)
