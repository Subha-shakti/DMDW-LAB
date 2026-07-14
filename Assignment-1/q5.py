def greatest(a,b,c):
    if(a>b and a>c):
        print(a," is greatest")
    elif(b>a and b>c):
        print(b, "is greatest")
    else:
        print(c,"is greatest")


a=input("enter 1st number  ")
b=input("enter 2nd number  ")
c=input("enter 3rd number  ")
greatest(a,b,c)
