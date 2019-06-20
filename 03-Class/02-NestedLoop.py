'''
for i in range(5):
    for j in range(5):
        print(i,j)
    print("J Exits")

print("Loop Exit")
'''

'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i):
        print('*',end='')
    print()

for i in range(8):
    for j in range(8-i):
        print(' ', end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()

for i in range(5):
    for j in range(i):
        print(i,end='')
    print()

