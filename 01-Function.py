x = 10
y = 20

# Function Definition
def calc():
    # Local Variables
    global x
    x = 12
    y = 33
    z = x + y
    print(z)
    return z

# Function Call
# calc()
# print(calc)
# print(calc())

a = calc()
print(a)

z = x + y
print(z)



