'''
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
'''

num = int(input("Enter the number : "))

for i in range(1,11):
    #print('{} x {} = {}'.format(num,i,num*i))
    print(f'{num} x {i} = {num*i}')


for i in range(2,21,2):
    print(i)
