d = {"a":10, "b":20, "c":30}

print("Keys:", d.keys())
print("Values:", d.values())
print("Items:", d.items())

d.update({"d":40})
print("After update:", d)

d.pop("b")
print("After pop:", d)

d.clear()
print("After clear:", d)