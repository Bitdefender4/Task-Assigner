import requests
import json
response = requests.get('https://www.boredapi.com/api/activity')
json_data = json.loads(response.text)
activity = json_data['activity']
peopleNeeded = json_data['participants']
cost = json_data['price']
typeO = json_data['type']
print("Activity: " + str(activity))
print("People needed: " + str(peopleNeeded))
print("Price: " + str(cost))
print("Type of activity: " + str(typeO))
#The price may not be accurate but you can complete a task with no cost if you want, just keep clicking run until the price is 0