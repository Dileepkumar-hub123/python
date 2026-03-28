s=input()
v=0
c=0
n=0
for ch in s:
    if ch=='a'or ch=='e'or ch=='i'or ch=='o' or ch=='u'or ch=='A' or ch=='E'or ch=='I'or ch=='O'or ch=='U':
        v=v+1
    elif ch.isdigit():
        n=n+1
    else:
        
        c=c+1
print("no of voles :",v)
print("no of consonts :",c)
print("no of numbers :",n)                
