
#a=['1','2','3']
#b=list(map(int,a))
#print(b,type(b))
#print(sum(b))

def maxi(x):
    return x%2!=0
a=[1,2,3,4,5,5,67]
b=filter(maxi,a)
print(list(b))


