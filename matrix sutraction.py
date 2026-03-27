a=[[2,3],[8,5]]
b=[[6,7],[7,4]]
result=[]
for i in range(len(a)):
    row=[]
    for j in range(len(a[0])):
        row.append(a[i][j]-b[i][j])
    result.append(row)
for r in result:
    print(r)