import math
n=int(input("enter :"))
root=int(math.sqrt(n))
if root*root==n:
  print("Perfect square")
else:
  print("not perfect square")