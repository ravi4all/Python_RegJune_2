# 1. Open File
# file = open('data_1.txt','r')

# 2. Read/Write
# data = file.read()
# print(data)

# 3. Close File
# file.close()


with open('data_2') as file:
    data = file.read()
    print(data)

