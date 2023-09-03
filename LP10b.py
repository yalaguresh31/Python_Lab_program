import json
with open('lob.json' , 'r') as file:
    data = json.load(file)
print("Current weather : ")
print("location : ",data['location'])
print("weather : ",data['weather'])
print("humidity : ",data['humidity'],"%")
print("Minimum temprature : ",data['temp_min'])
print("Maximum temprature : ",data['temp_max'])