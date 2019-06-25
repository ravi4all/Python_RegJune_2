data = [
    {"name":"Ram","grade":"A","marks":[45,56,78]},
    {"name":"Raman","grade":"B","marks":[55,66,78]},
    {"name":"Aman","grade":"A+","marks":[75,50,83]},
    {"name":"Sita","grade":"A+","marks":[49,68,73]},
    {"name":"Geeta","grade":"B","marks":[78,87,79]}
    ]

for i in range(len(data)):
    if data[i]['grade'] == 'A+':
        print(data[i]["name"], data[i]["grade"],data[i]["marks"])

for i in range(len(data)):
    marks = data[i]["marks"]
    avg = sum(marks) // len(marks)
    print("Average marks of {} is {}".format(data[i]["name"], avg))
