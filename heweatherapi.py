import sys
import json
from urllib import urlencode
import urllib2
from utils import consts

def getLocation():
	"""get location from user input
	default xiqing
	"""
	argvs = sys.argv
	location = argvs[1] if len(argvs) >= 2 else consts.HEWEAPI.LOCATION_CODE
	return location
	
def fetchWeather(location):
	params = urlencode({
        'key': consts.HEWEAPI.KEY,
        'city': location,
        'lang': consts.HEWEAPI.LANGUAGE,
    })
	req = urllib2.Request('{api}?{params}'.format(api=consts.HEWEAPI.URL_FREE_API, params=params))
	response = urllib2.urlopen(req,timeout=5).read().decode('UTF-8')
	return response
	
if __name__ == '__main__':
	location = getLocation()
	try:
		resultS = fetchWeather(location)
	except Exception,e:#urllib2.HTTPError,urllib2.URLError...
		print str(e)
		continue
	else:
		resultD = json.loads(resultS)
		status_code = resultD['HeWeather5'][0]['status']
		if(consts.HEWEAPI.STATUS_INFO.has_key(status_code)):
			temp = resultD['HeWeather5'][0]['now']['tmp']
			humi = resultD['HeWeather5'][0]['now']['hum']
			print temp,humi
		else:
			print consts.HEWEAPI.ERROR_INFO[status_code].decode('UTF-8')		