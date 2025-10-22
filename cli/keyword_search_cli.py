#!/usr/bin/env python3

import argparse

from lib.utils import keyword_search


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

            for idx, movie in enumerate(matching_movies, start=1):
                print(f"{idx}. {movie['title']}")
            pass
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
