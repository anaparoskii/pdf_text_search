from search_engine import search_phrase, search_words
from paragraph import print_result
from rank import rank


def words_search(trie, words, hashmap, graph):
    print("Search results:\n")
    result = search_words(trie, words, graph, hashmap)
    if len(result) > 0:
        if isinstance(result[0], tuple):
            sorted_pages = result
        else:
            sorted_pages = rank(result, graph)
        print_result(sorted_pages, hashmap, words, 1)
    else:
        print("No results found")


def phrase_search(phrase, hashmap, graph):
    print("Search results:\n")
    result = search_phrase(phrase, hashmap)
    if len(result) > 0:
        sorted_pages = rank(result, graph)
        print_result(sorted_pages, hashmap, phrase, 0)
    else:
        print("No results found")
