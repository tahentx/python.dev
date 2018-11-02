import requests

def main():
	url = "https://monitoringapi.solaredge.com/sites/list?api_key=XUR0SMGADU7Y2NY4M2R7ZOS3KJ5WXSR4"
	api_key = {'key': 'XUR0SMGADU7Y2NY4M2R7ZOS3KJ5WXSR4'}
	response = requests.get(url, params=api_key)
	print(response.text)

if __name__ == "__main__":
		main()

