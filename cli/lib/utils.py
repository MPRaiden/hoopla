import json


def keyword_search(keyword, sourceFile):
    results = []

    with open(sourceFile, "r") as file:
        data = json.load(file, strict=False)

    for movie in data["movies"]:
        if keyword in movie["title"]:
            results.append(movie)

    sorted_results = sorted(results, key=lambda m: m["id"])

    return sorted_results[0:5]
