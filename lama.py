
#a=['1','2','3']
#b=list(map(int,a))
#print(b,type(b))
#print(sum(b))

def maxi(x):
    return x.startswith('c')
a=['cat','call','bat','commit']
a.append('cricket')
b=filter(maxi,a)
print(tuple(b))


