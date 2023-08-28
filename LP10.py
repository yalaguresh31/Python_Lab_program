#10) B) Write a python program to fetch current weather data from the JSON file.
#Source Code:
#JSON File:
{
"coord": {
"lon":-122.08.
"lat":37.39
}.
 "weather": [
    {
"id": 800,
"main": "Clear",
"description": "clear" 
"icon": "Old"
    }
 ],
"base": "stations",
"main":{
"temp": 22.0.
"feels like": 22.0, 
"temp_min": 20.0,
"temp_max":240,
"pressure": 1018, 
"humidity": 50
},
"visibility": 10000. 
"wind": {
"speed": 4.6,
 "deg": 330
},
"clouds":{
"all":1
},
 "dt": 1619021689,
"sys":{
 "type": 1,
"id": 5122,
"country":"US",
"sunrise": 1619008936,
"sunset": 1619056278
},
"timezone":-25200,
"id": 420006353,
"name": "San Francisco",
"cod": 200
}
#Python File:
 import json
#Open the ISON file
with open(weather data.json', 'r') as file:
#Load the JSON data into a dictionary data = json.load(file)
#Extract the current temperature from the dictionary 
current_temp = data['main']['temp']
#Print the current temperature
print("The current temperature is {current_temp} degrees Celsius.")
