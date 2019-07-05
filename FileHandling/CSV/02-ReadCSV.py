import csv
import pandas as pd

data = []

with open('users.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        d = {"name":row[0], "email":row[1], "pwd":row[2], "city":row[3]}
        data.append(d)

# print(data)
data = pd.read_csv("users.csv", header=None)
data.columns = ['name','email','pwd','city']
print(data)