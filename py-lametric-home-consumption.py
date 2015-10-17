#!/usr/bin/python

from DALClient import DALClient
from LaMetricClient import LaMetricClient
import json
import ConfigParser


config = ConfigParser.RawConfigParser()
config.read('py-lametric-home-consumption.properties')

dal_ip = config.get('DAL', 'dal_ip');
dal_port = config.get('DAL', 'dal_port');
dal_addr=dal_ip + ":" + dal_port
print dal_addr
device = config.get('DAL', 'device');
function = config.get('DAL', 'function');
property = config.get('DAL', 'property');

mydal = DALClient.DALClient(dal_addr);
res = mydal.request_property_read(device,function,property);
res = json.loads(res)
power = res['level']

icon = ""

if(power < 500):
	icon = "i275"
elif (power < 1000):
	icon = "i904"	
else:
	icon = "i660"

token = config.get('LAMETRIC', 'token');
path = config.get('LAMETRIC', 'path');

lametric = LaMetricClient.LaMetricClient(token,path)

lametric.publish(power,icon);
