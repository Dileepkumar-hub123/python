# write a python program to find electric bill based on following rate
#0-50 (0.50)
# 51-150 (0.75)
# 151-250 (1.20)
# >250 (1.75)
n=float(input("enter electric bill:"))
if(n>=50):
    print(n*0.5)
elif (n<50 and n>=150):
    print("25+(n-50)*0.75")
elif(n>150 and n<+250):
    print("100+(n-150)*1.2")
else :
    print("220+(n-250)*1.75")    