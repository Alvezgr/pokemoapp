import requests

def get_pokemons(url='http://pokeapi.co/api/v2/pokemon/'):
	
	#args = {'offset': offset} if offset else {}
	response = requests.get(url)
	if response.status_code == 200:
		payload = response.json()
		
		return payload

if __name__ == '__main__':
	url = 'http://pokeapi.co/api/v2/pokemon-form/'
	print(get_pokemons())
	print(type(get_pokemons()))
	