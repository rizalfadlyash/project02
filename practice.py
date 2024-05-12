import requests

api_key = '5bc0bec0-a6f2-47a4-a72b-35a12a53b47b'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

# Lakukan permintaan HTTP dan simpan respons dalam variabel res
res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)
