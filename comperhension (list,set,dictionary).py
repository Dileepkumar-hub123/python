a=[1,2,3,4,5,6,7,8,9,10,2]
b=[i*i for i in a]
c={i*i  for i in a}
d={i:i*i for i in a}
e=sorted(c)
print(b)
print(e)
print(d)