def refact(c):
    if c==0:
        return 1
    else:
        return c*refact(c-1)
print(refact(5))    