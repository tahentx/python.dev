import requests
import json

# dpath might be the library to use to pull data from complex dictionary
# url and api key to test solaredge api
def main():
	url = "https://app.smartsheet.com/b/home?lx=GYHFpeSnjeyOZXV5k2SRGA"
	api_key = {'api_key': 'j3ashfc8ezwkan27jger2l4ewx'}
# first use of requests library
	response = requests.get(url,params=api_key)
	print(response.text)
	
	

if __name__ == "__main__":
		main()
# api_key=XUR0SMGADU7Y2NY4M2R7ZOS3KJ5WXSR4

