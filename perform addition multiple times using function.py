def sum(a,b):
    return a+b
n=int(input("enter number of addition:"))
for i in range(n):
    a,b=map(int,input().split())
    print("addition is :",sum(a,b))
