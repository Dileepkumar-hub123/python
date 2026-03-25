n = int(input("Enter n value: "))
a = []

for i in range(n):
    num = int(input())
    a.append(num)

key = int(input("Enter key value: "))

found =1

for i in range(n):
    if a[i] == key:
        print("Element is found at position:", i + 1)
        found =0
        break

if found==1:
    print("Element not found")