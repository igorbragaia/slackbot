from watson_developer_cloud import NaturalLanguageClassifierV1, WatsonApiException

default_end_point = 'https://gateway.watsonplatform.net/natural-language-classifier/api'

natural_language_classifier = NaturalLanguageClassifierV1(
    username='{username}',
    password='{password}',
    url='https://gateway-fra.watsonplatform.net/natural-language-classifier/api'
)

my_word = input("Write a word to be read: ")


try:
    print(my_word)
except WatsonApiException as ex:
    print ("Method failed with status code " + str(ex.code) + ": " + ex.message)