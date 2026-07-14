def fib(n):
    a=0
    b=1
    print("fib series")
    for i in range(n):
        print(a,end="")
        c=a+b
        a=b
        b=c
n=int(input("enter a num of turms"))
fib(n)     
