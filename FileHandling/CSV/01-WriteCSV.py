import csv
# csv - comma seperated values

users = [
    {"name":"Ram","email":"ram@gmail.com","pwd":1234,"city":"Delhi"},
    {"name":"Shyam","email":"shyam@gmail.com","pwd":1234,"city":"Delhi"},
    {"name":"Mohan","email":"mohan@gmail.com","pwd":1234,"city":"Delhi"},
    {"name":"Aman","email":"aman@gmail.com","pwd":1234,"city":"Delhi"},
    {"name":"Suman","email":"suman@gmail.com","pwd":1234,"city":"Delhi"},
]

with open('users.csv','w', newline='') as file:
    writer = csv.writer(file)
    for row in users:
        writer.writerow(row.values())
