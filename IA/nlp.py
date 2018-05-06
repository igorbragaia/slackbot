import requests
from pprint import pprint
from IA.keys import Keys


class NLP:
    name = 'Text_Categorization'
    key1 = Keys.key1
    key2 = Keys.key2
    subscription_key = key1
    text_analytics_base_url = 'https://brazilsouth.api.cognitive.microsoft.com/text/analytics/v2.0/'
    key_phrase_api_url = text_analytics_base_url + "keyPhrases"
    sentiment_api_url = text_analytics_base_url + "sentiment"
    entity_linking_api_url = text_analytics_base_url + "entities"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    id = 1

    @classmethod
    def get_key_phrases(cls, data):
        documents = {'documents': []}

        for text in data:
            aux = {}
            aux['id'] = cls.id
            cls.id += 1
            aux['language'] = 'pt-BR'
            aux['text'] = text
            documents['documents'].append(aux)

        response = requests.post(cls.key_phrase_api_url, headers=cls.headers, json=documents)
        key_phrases = response.json()['documents']

        my_list = []
        for obj in key_phrases:
            my_list.append(obj['keyPhrases'])

        return my_list

    @classmethod
    def get_sentiments(cls, data):
        documents = {'documents': []}

        for text in data:
            aux = {}
            aux['id'] = cls.id
            cls.id += 1
            aux['language'] = 'pt-PT'
            aux['text'] = text
            documents['documents'].append(aux)

        response = requests.post(cls.sentiment_api_url, headers=cls.headers, json=documents)
        sentiments = response.json()

        return sentiments

# Example on how to do it:
# should be passed a vector of strings to be analized.
# The entire vector is counted just as one request! Be careful to not do to many requests!
# Try to use as many strings in one vector as possible, and not vector with just one string

# documents = [
#   'Ruby on Rails',
#   'Quero aprender Python3',
#   'C++ como linguagem',
#   'Queria aprender lideranca, processamento de sinais e analise de dados',
#   'React Native',
#   'Elixir Day Quero Educacao'
# ]
#
# key_phrases = NLP.get_key_phrases(documents)
# pprint(key_phrases)
