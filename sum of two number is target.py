def sum(s,t):
    l=len(s)
    for i in range(l):
        for j in range(i+1,l):
             if (s[i]+s[j]==t) :
                 return [i,j]
n = int(input("Enter size of list: "))
s = []
print("enter elemens:")
for i in range(n):
    num = int(input())
    s.append(num)

t=int(input("enter target value:"))
r=sum(s,t)  
print(r)