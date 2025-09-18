a=list(map(int,input().split(",")))    #a = list(map(int, input().split(",")))


f=[0]
for i in a:
    c=[]
    for s in f:
        c.append(s+i)
    f.extend(c)
print(f)    