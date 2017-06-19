import sys
import json
from urllib import urlencode
import urllib2
from utils.heweather_const_value import KEY,LOCATIONCODE,FREEAPI,LANGUAGE

def getLocation():
	"""get location from user input
	default xiqing
	"""
	argvs = sys.argv
	location = argvs[1] if len(argvs) >= 2 else LOCATIONCODE
	return location
	
def fetchWeather(location):
	params = urlencode({
        'key': KEY,
        'city': location,
        'lang': LANGUAGE,
    })
	req = urllib2.Request('{api}?{params}'.format(api=FREEAPI, params=params))
	response = urllib2.urlopen(req,timeout=5).read().decode('UTF-8')
	return response
	
if __name__ == '__main__':
	location = getLocation()
	resultS = fetchWeather(location)
	resultD = json.loads(resultS)
	if(resultD['HeWeather5'][0]['status'] == 'ok'):
		temp = resultD['HeWeather5'][0]['now']['tmp']
		humi = resultD['HeWeather5'][0]['now']['hum']
	print status,temp,humi