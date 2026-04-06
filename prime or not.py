n=int(input("enter n :"))
f=0
for i in range(1,n+1):
    if(n%i==0):
     f=f+1
     if(f>2):
        print("not prime number ")
        break
if f==2 :
    print("prime number")
        
        