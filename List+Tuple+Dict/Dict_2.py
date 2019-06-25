data = {
    "names" : ["Sachin","Kohli","Rohit","Dhawan","Dhoni","Raina"],
    "scores" : [56,65,67,102,110,59],
    "strike_rate" : [101.3,110.2,104.2,98.7,99.5,105.5]
    }

for i in range(len(data["scores"])):
    if data["scores"][i] > 60:
        print(data["names"][i], data["scores"][i])
