#What is string formatting in Python?
a='Dileep'
b=342
c=3.1417
print("my name is %s and %.4d is my roll no"%(a,b))
print("my name is {1} and {0} is my roll no".format(b,a))
print(f"{c:.2f}")