#API key for wunderground: cb89ade5f98c2a45 
import requests

r = requests.get("http://api.wunderground.com/api/cb89ade5f98c2a45/conditions/forecast/q/France/Paris.json")
data = r.json()

location = data['current_observation']['display_location']['full']
temp = data['current_observation']['temp_c']
feelslike = data['current_observation']['feelslike_c']

print "Currently in " + location + " it is: " + str(temp) + " degrees. But it feels like " + str(feelslike) + " degrees"

if temp < 9:
    print "Better bring a jacket to be warm"
if temp > 23:
    print "It's pretty warm. Stay cool!"
    
print ""

print "Here's what is happening in the next 4 days:"

for day in data['forecast']['simpleforecast']['forecastday']:
    print day['date']['weekday'] + "," + day['date']['monthname'] + str(day['date']['day']) + ":"
    print "Conditions: ", day['conditions']
    print "High: ", day['high']['celsius'] + "C", "Low: ", day['low']['celsius'] + "C"
    print ""
