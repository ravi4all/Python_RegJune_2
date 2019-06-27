def add(*x):
    c = 0
    for num in x:
        c += num
    print(c)

add(3,4,5,6)
add(5,6,8,8,4,4,6)
add(2,3,5,65,23,67)

def emp(id,name,sal,*address):
    print("Id :",id)
    print("Name :",name)
    print("Salary ",sal)
    print("Address :",address)

emp(101,'Ram',34000,'Delhi')
emp(101,'Ram',34000,'Delhi','Mumbai')
emp(101,'Ram',34000,'Delhi','Pune','Mumbai')