def average(a):
    return sum(a)//len(a)

a=list(map(int,input().split()))
t=average(a)
print("average:",t)