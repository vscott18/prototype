#API key for wunderground: cb89ade5f98c2a45 
import requests

r = requests.get("http://api.wunderground.com/api/cb89ade5f98c2a45/forecast/q/France/Paris.json")

data = r.json()

print data.keys()