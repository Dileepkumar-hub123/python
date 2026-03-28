s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0

for ch in s:
    if ch in 'aeiouAEIOU':
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1

print("No. of vowels:", vowels)
print("No. of consonants:", consonants)
print("No. of digits:", digits)