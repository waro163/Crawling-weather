#!/usr/bin/python

import random
import MySQLdb
import time
import heweatherapi
import json
from utils import consts

UPDATE_INTERVAL = 10;

conn = MySQLdb.connect(
	host = 'localhost',
	port = 3306,
	user = 'root',
	passwd = 'helloworld',
	db = 'pvcgdb'
	);

cur = conn.cursor();
sqli = "insert into 433mesh (node_id,temp,humidity,hops) values(%d, %.2f, %.2f, '%s')";

node_dict={12:1,28:1,15:1,16:1,19:16}
temp = 25
humi = 20
while (1):
	location = heweatherapi.getLocation()
	try:
		resultS = heweatherapi.fetchWeather(location)
	except Exception,e:
		print str(e)
		continue
	else:
		resultD = json.loads(resultS)
		status_code = resultD['HeWeather5'][0]['status']
		if(consts.HEWEAPI.STATUS_INFO.has_key(status_code)):
			temp = resultD['HeWeather5'][0]['now']['tmp']
			humi = resultD['HeWeather5'][0]['now']['hum']
		else:
			print consts.HEWEAPI.ERROR_INFO[status_code].decode('UTF-8')
			continue
		for node_key in node_dict.keys():
			hops_val=[]
			hops_val.append(node_key)
			while(hops_val[-1] != 1):
				hops_val.append(node_dict[hops_val[-1]])
			hops_str = ','.join(map(str, hops_val))
			#print hops_str
			temp_t = int(temp) + round(random.random(),2)
			humi_t = int(humi) - round(random.random(),2)
			#print sqli % (node_key,temp_t,humi_t,hops_str)
			cur.execute(sqli % (node_key,temp_t,humi_t,hops_str))
			conn.commit()
			time.sleep(UPDATE_INTERVAL)
#	time.sleep(UPDATE_INTERVAL)

cur.close();
conn.close();

