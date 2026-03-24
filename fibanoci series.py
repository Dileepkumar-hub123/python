#write a python program to creat fibanoic series
n=int(input("enter n :"))
i=2
f=0
s=1
print(f)
print(s)
while i<n:
    t=f+s
    print(t)
    f=s
    s=t
    i=i+1
    