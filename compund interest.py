p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))

A = p * (1 + r/100) ** t

print("Compound Interest =", A - p)
