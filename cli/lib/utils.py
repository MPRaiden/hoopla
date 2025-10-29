import json
import string


def keyword_search(keyword, sourceFile):
    results = []

    with open(sourceFile, "r") as file:
        data = json.load(file, strict=False)

    for movie in data["movies"]:
        clean_keyword = search_input_cleanup(keyword)
        clean_title = search_input_cleanup(movie["title"])

        if clean_keyword in clean_title:
            results.append(movie)

    sorted_results = sorted(results, key=lambda m: m["id"])

    return sorted_results[0:5]


def search_input_cleanup(input):
    input = input.lower()
    remove_punc = str.maketrans("", "", string.punctuation)
    input = input.translate(remove_punc)

    return input
