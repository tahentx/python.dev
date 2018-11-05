import requests
import json
import dpath.util
# dpath might be the library to use to pull data from complex dictionary
# url and api key to test solaredge api
def main():
	url = "https://monitoringapi.solaredge.com/sites/list?"
	api_key = {'api_key': 'XO272VFG4MWNJM1LTOSX6G0E2OUA19XA'}
# first use of requests library
	response = requests.get(url, params=api_key)
	data = json.loads(response.text)
	project = data['sites']['site']
	for data in project:
		print(project['modelName'])

if __name__ == "__main__":
		main()
# api_key=XUR0SMGADU7Y2NY4M2R7ZOS3KJ5WXSR4

