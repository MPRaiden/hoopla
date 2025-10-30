import json
import string


def keyword_search(keyword, sourceFile):
    results = []

    with open(sourceFile, "r") as file:
        data = json.load(file, strict=False)

    for movie in data["movies"]:
        clean_query = search_input_cleanup(keyword)
        clean_title = search_input_cleanup(movie["title"])

        # checks if the title contains the query
        found_match = False

        for token in clean_query:
            for title in clean_title:
                if token in title:
                    found_match = True
                    break
            if found_match:
                break
        if found_match:
            results.append(movie)

    sorted_results = sorted(results, key=lambda m: m["id"])

    return sorted_results[0:5]


def search_input_cleanup(input):
    # handles casing
    input = input.lower()

    # removes punctuation
    remove_punc = str.maketrans("", "", string.punctuation)
    input = input.translate(remove_punc)

    # tokenizes and removes empty tokens
    tokens = input.split(" ")
    tokens = [token for token in tokens if token != ""]

    return tokens
