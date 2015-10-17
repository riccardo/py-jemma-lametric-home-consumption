import urllib, urllib2
import json


class LaMetricClient(object):
	
	def __init__(self,token,mypath):
		self.token=token
		self.mypath=mypath
		pass

	def publish(self,power,icon):
		print "posting [power="+str(power)+"] [icon="+icon+"]"
		opener = urllib2.build_opener();
		headers = { 'Accept': 'application/json', 'Cache-Control': 'no-cache', 'X-Access-Token': self.token  };
		mytext = str(power) + " W"
		posttext='{"frames": [{"index": 0,"text": "'+mytext+'","icon": "'+icon+'"}]}'
		req = urllib2.Request(self.mypath, posttext ,headers);
		response = opener.open(req);
		if(response.getcode()==200):
			print "ok"
		else:
			print "error code:" + response.getcode() + " on call to " + mypath	
