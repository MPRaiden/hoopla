#!/usr/bin/env python3

import argparse
import json


def keyword_search(keyword, sourceFile):
    results = []

    with open(sourceFile, "r") as file:
        data = json.load(file, strict=False)

    for movie in data["movies"]:
        if keyword in movie["title"]:
            results.append(movie)

    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            matching_movies = keyword_search(args.query, "data/movies.json")

            count = 1
            for movie in matching_movies:
                print(f"{count}. Movie title {movie["title"]}")
                count += 1
            pass
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
