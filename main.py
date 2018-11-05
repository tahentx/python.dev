import requests
import json
import dpath.util
# dpath might be the library to use to pull data from complex dictionary
# url and api key to test solaredge api
def main():
	url = "http://demo.solarlog-web.net/api?username=812045917&password=ufntoedz&solarlog=9&function=getMinuteValues&format=json&date"
	# api_key = {'api_key': 'XO272VFG4MWNJM1LTOSX6G0E2OUA19XA'}
# first use of requests library
	response = requests.get(url)
	print(response.text)
	# data = json.loads(response.text)
	# project = data['sites']['site']
	# for data in project:
	# 	print(project['modelName'])

if __name__ == "__main__":
		main()
# api_key=XUR0SMGADU7Y2NY4M2R7ZOS3KJ5WXSR4

