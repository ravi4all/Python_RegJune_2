# Map Function
def temp_conv(cel):
    return 9/5 * cel + 32

# f = temp_conv(43.5)
# print(f)

temp = [34.5,43.5,43.2,42.6,39.8]

# f = []
# for t in temp:
#     f.append(temp_conv(t))
#
# print(f)

f = list(map(temp_conv,temp))
print(f)

def myMap(func, iter):
    data = []

    for i in range(len(iter)):
        data.append(func(iter[i]))

    return data

f = myMap(temp_conv, temp)
print(f)












