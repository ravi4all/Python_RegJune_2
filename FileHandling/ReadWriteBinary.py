file = open('bahubali.jpg','rb')
data = file.read()
print(len(data))
# print(data)
file.close()

file = open('img_2.jpg','wb')
file.write(data)
file.close()