words= ["mass","as","hero","heroin","prince","princess"]
result =[]
for i in range(len(words)):
    for j in range(len(words)):
        if i !=j and words[i] in words[j]:
            result.append(words[i])
            break
print("matching words are:", result)