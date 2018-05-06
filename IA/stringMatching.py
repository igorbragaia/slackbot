from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def string_match(search_word, data_words):
    if type(data_words) == str:
        data_words = [data_words]

    similarity = [similar(search_word, word) for word in data_words]

    if len(similarity) == 0 or max(similarity) == 1:
        return search_word
    elif max(similarity) > 0.5:
        return data_words[similarity.index(max(similarity))]
    else:
        return ''
        # return "Nenhum resultado encontrado. Deseja iniciar um topico para "+ searchWord+ "?"
    # values.index(max(similarity))


if __name__ == "__main__":
    lng = ["ruby", "freaking fair", "c++", "iurbriubirub", "r o r", "ror", "Ruby Sinatra", "raoubi", "iiiiii"]
    x = string_match("c++ eita ruby", lng)
    print(x)
