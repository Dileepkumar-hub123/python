n=int(input("enter n :"))
sd=0
pd=1
while n!=0 :
 d=n%10
 sd=sd +d
 pd=pd*d
 n=n//10
if(sd==pd):
 print("spy number")
else:
 print("not spy number")  
