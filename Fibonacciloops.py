n=int(input("enter a fibonacci number greater than 2"))
fib1=0
fib2=1
for i in range(3,n+1):
    fib3=fib1+fib2
    fib1=fib2
    fib2=fib3
print(fib3)
