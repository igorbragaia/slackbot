import requests
from pprint import pprint

name = 'Text_Categorization'
key1 = 'da4c0ff09c204cf09a8fef9ac45d34e5'
key2 = '23f5f4d3b03b4cfd83fd74486f544286'
subscription_key = key1
text_analytics_base_url = 'https://brazilsouth.api.cognitive.microsoft.com/text/analytics/v2.0/'

key_phrase_api_url = text_analytics_base_url + "keyPhrases"
sentiment_api_url = text_analytics_base_url + "sentiment"
entity_linking_api_url = text_analytics_base_url + "entities"

headers = {"Ocp-Apim-Subscription-Key": subscription_key}

documents = {'documents' : [
  {'id': '1', 'language': 'pt-BR', 'text': 'Ruby on Rails'},
  {'id': '2', 'language': 'pt-BR', 'text': 'Quero aprender Python3'},
  {'id': '3', 'language': 'pt-BR', 'text': 'C++ como linguagem'},
  {'id': '4', 'language': 'pt-BR', 'text': 'Gosto da linguagem C#'},
  {'id': '5', 'language': 'pt-BR', 'text': 'React Native'},
  {'id': '6', 'language': 'pt-BR', 'text': 'Elixir Day Quero Educacao'},
]}

print("Key Phrases:")
response = requests.post(key_phrase_api_url, headers=headers, json=documents)
pprint(response)
key_phrases = response.json()
pprint(key_phrases)
print("")
