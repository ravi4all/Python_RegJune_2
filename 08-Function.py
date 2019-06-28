# Closures
def outer():
    x = 12
    def add():
        y = 32
        z = x + y
        return z
    def sub():
        y = 21
        z = x - y
        return z
    # print(add())
    # print(sub())
    return add,sub

# z = outer()
# print(z)

a = outer()[0]()
print(a)