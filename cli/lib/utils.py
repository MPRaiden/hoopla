import json
import string
from nltk.stem import PorterStemmer


def keyword_search(keyword, sourceFile):
    stopwords = get_stopwords("data/stopwords.txt")

    with open(sourceFile, "r") as file:
        data = json.load(file, strict=False)

    # Clean query ONCE before the loop
    clean_query = search_input_cleanup(keyword, stopwords)

    results = []
    for movie in data["movies"]:
        clean_title = search_input_cleanup(movie["title"], stopwords)

        if any(
            token in title_token for token in clean_query for title_token in clean_title
        ):
            results.append(movie)

    return sorted(results, key=lambda m: m["id"])[:5]


def search_input_cleanup(input, stopwords=None):
    # handles casing
    input = input.lower()

    # removes punctuation
    remove_punc = str.maketrans("", "", string.punctuation)
    input = input.translate(remove_punc)

    # tokenizes and removes empty tokens
    tokens = input.split(" ")
    tokens = [token for token in tokens if token != ""]

    # removes stopwords
    if stopwords:
        tokens = [token for token in tokens if token not in stopwords]

    # stem
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]

    return tokens


def get_stopwords(file):
    with open(file, "r") as f:
        return set(f.read().splitlines())
