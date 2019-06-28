def calc(x,y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a,b,c,d

# i = calc(4,5)
# print(i)

# Packing Unpacking
# i,j,k,l = calc(4,5)
# print(i,j,k,l)

i,j,*k = calc(4,5)
print(i,j,k)