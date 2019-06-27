def add(x,y):
    z = x + y
    print("sum is",z)
def sub(x,y):
    z = x - y if x > y else y - x
    print("diff is",z)
def div(x,y):
    z = x / y
    print("div is",z)
def mul(x,y):
    z = x * y
    print("mul is",z)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = input("Enter your choice : ")
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

operations = {
    "1" : add,
    "2" : sub,
    "3" : div,
    "4" : mul
}
operations[ch](num_1, num_2)


