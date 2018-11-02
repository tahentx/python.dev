import requests

def main():
	url = "https://monitoringapi.solaredge.com/sites/list?"
	api_key = {'api_key': '00B0NBZ03D5X517UX7UFJW3PSKFA4BUL'}
	response = requests.get(url, params=api_key)
	print(response.text)

if __name__ == "__main__":
		main()
# api_key=XUR0SMGADU7Y2NY4M2R7ZOS3KJ5WXSR4
