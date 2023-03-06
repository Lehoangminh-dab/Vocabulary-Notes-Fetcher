import requests
import json
import pprint

# TODO: replace with your own app_id and app_key
app_id = 'ea922d64'
app_key = 'edbfdb7a36ad5ddc74ff45f439367cf5'
language = 'en-gb'
print("Bruh type the word in here")
word_id = input()
fields = 'definitions,examples,pronunciations'
strictMatch = 'false'

url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
vocab=json.loads(r.text)
pprint.pprint (vocab)
#print word + " (<adj,v,n,etc..>) " + ":"
