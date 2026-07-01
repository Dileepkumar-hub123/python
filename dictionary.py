print("enter no of students:")
n=int(input())
a={}

for i in range(n):

    c=input("enter name:")
    d=int(input("enter mark:"))
    a[c]=d
    
for name, mark in a.items():
    print(name, mark)

    