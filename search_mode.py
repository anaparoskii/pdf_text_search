from search_engine import get_paragraph, search_phrase, search_words, rank


def words_search(trie, words, hashmap, graph):
    print("Search results:\n")
    result = search_words(trie, words, graph, hashmap)
    if len(result) > 0:
        if isinstance(result[0], tuple):
            sorted_pages = result
        else:
            sorted_pages = rank(result, graph)
        print(f"Results found: {len(sorted_pages)}\n")
        max_i = 25
        i = 1
        for page, count in sorted_pages:
            if i > max_i:
                choice = input("Press Enter to continue or X to terminate... ")
                if choice.lower() == "x":
                    break
                else:
                    max_i += 25
            paragraph = get_paragraph(hashmap[page], words, 1)
            count = round(count)
            print(f"{i}: Page {page} - {count} occurrences\n{paragraph}\n")
            i += 1
    else:
        print("No results found")


def phrase_search(phrase, hashmap, graph):
    print("Search results:\n")
    result = search_phrase(phrase, hashmap)
    if len(result) > 0:
        sorted_pages = rank(result, graph)
        max_i = 25
        i = 1
        for page, count in sorted_pages:
            if i > max_i:
                choice = input("Press Enter to continue or X to terminate... ")
                if choice.lower() == "x":
                    break
                else:
                    max_i += 25
            paragraph = get_paragraph(hashmap[page], phrase, 0)
            print(f"{i}: Page {page} - {count} occurrences\n{paragraph}\n")
            i += 1
    else:
        print("No results found")
