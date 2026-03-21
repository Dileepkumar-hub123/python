# amstrong number or not
n=int(input("enter n :"))
temp=n
sum=0
p=len(str(n))
while n!=0:
    rem=n%10
    sum=sum + rem**p
    n=n//10
if temp==sum:
    print("amstrong")
else :
    print("not amstrong")