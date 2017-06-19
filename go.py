#!/usr/bin/python

import random
import MySQLdb
import time
import heweatherapi
import json

UPDATE_INTERVAL = 180;

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
	resultS = heweatherapi.fetchWeather(location)
	resultD = json.loads(resultS)
	if(resultD['HeWeather5'][0]['status'] == 'ok'):
		temp = resultD['HeWeather5'][0]['now']['tmp']
		humi = resultD['HeWeather5'][0]['now']['hum']
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
		time.sleep(5)
	time.sleep(UPDATE_INTERVAL)

cur.close();
conn.close();

