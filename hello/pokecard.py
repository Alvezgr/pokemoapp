import requests
import random

def get_card():
	ide = random.randint(1,802)
	url = 'https://pokeapi.co/api/v2/pokemon/'+ str(ide) + '/'
	response = requests.get(url)

	if response.status_code == 200:
		payload = response.json()
		return payload
if __name__ == '__main__':
	print(get_card())