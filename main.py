import requests
import json

def main():
	url = "https://monitoringapi.solaredge.com/sites/list?"
	api_key = {'api_key': 'XO272VFG4MWNJM1LTOSX6G0E2OUA19XA'}

	response = requests.get(url, params=api_key)
	data = json.loads(response.text)
	print(type(data))

if __name__ == "__main__":
		main()
# api_key=XUR0SMGADU7Y2NY4M2R7ZOS3KJ5WXSR4

