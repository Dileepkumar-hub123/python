def is_anagram(a,b):
    return sorted(a)==sorted(b)
a=input("enter a string:")
b=input("enter a another string:")
if is_anagram(a,b):
    print("valid anagram")
else:
    print("invalid anagram")    