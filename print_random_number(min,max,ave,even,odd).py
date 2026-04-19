import random
num=[random.randint(1,100) for i in range (20)]
print(num)
print("minimum number is :",min(num),)
print("maximum number is:",max(num))
print("average number is :",sum(num)/len(num))
even=0
odd=0
for i in num :
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1    
print("number of even number:",even)  
print("number of odd numbers",odd)      
