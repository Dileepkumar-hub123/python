n=int(input("enter n value:"))
a=[]
print("enter list:")
for i in range(n):
    num=int(input())
    a.append(num)
m=[i*i for i in a]
print(m)