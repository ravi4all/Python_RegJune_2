file = open('data_1.txt')

# will read till 10th character
# data = file.read(10)

# will read one line at a time
# data = file.readline()

# will read all the lines and return a list
# data = file.readlines()

file.seek(20)
data = file.read()
print(data)

file.close()