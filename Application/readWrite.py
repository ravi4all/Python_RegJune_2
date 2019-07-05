import csv

def readData():
    pass

def writeData(data):
    with open('users.csv','a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.values())