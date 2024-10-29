import requests

api_key = 'e2fdbc6a-2c18-4d7a-b60a-99b0dc2083a2'
word = ' potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()


for definition in definitions:
    print(definition)