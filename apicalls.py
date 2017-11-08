#API key for wunderground: cb89ade5f98c2a45 
import requests

firstPart = "http://api.wunderground.com/api/cb89ade5f98c2a45/conditions/forecast/q/"
query = "Paris/France"
getThis = firstPart+query + ".json"

#r = requests.get(getThis)
#data = r.json()

print getThis
#location = data['current_observation']['display_location']['full']
#temp = data['current_observation']['temp_c']
#feelslike = data['current_observation']['feelslike_c']
#
#print "Currently in " + location + " it is: " + str(temp) + " degrees. But it feels like " + str(feelslike) + " degrees"
#
#if temp < 9:
#    print "Brrr! It's pretty cold. Better bring a jacket to stay warm."
#if temp > 23:
#    print "Is it just the weather or did you just walk in? Either case, it's hot right now. Stay cool!"
#    
#print ""
#
#print "Here's what is happening in the next 4 days:"
#
#for day in data['forecast']['simpleforecast']['forecastday']:
#    print day['date']['weekday'] + ", " + day['date']['monthname'] + " " + str(day['date']['day']) + ":"
#    print "Conditions: ", day['conditions']
#    print "High: ", day['high']['celsius'] + "C", "Low: ", day['low']['celsius'] + "C"
#    print ""
