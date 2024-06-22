from search_engine import search_result, get_paragraph


def words_search(graph, words, hashmap):
    print("Search results:\n")
    result = graph.search_words(words)
    if result:
        sorted_pages = search_result(result)
        max_i = 50
        i = 1
        for page, count in sorted_pages:
            if i > max_i:
                choice = input("Press Enter to continue or X to terminate... ")
                if choice.lower() == "x":
                    break
                else:
                    max_i += 50
            paragraph = get_paragraph(hashmap[page], words, 1)
            print(f"{i}: Page {page} - {count} occurrences\n{paragraph}\n")
            i += 1
    else:
        print("No results found")


def phrase_search(graph, phrase, hashmap):
    print("Search results:\n")
    result = graph.search_phrase(phrase, hashmap)
    if len(result) > 0:
        sorted_pages = search_result(result)
        max_i = 50
        i = 1
        for page, count in sorted_pages:
            if i > max_i:
                choice = input("Press Enter to continue or X to terminate... ")
                if choice.lower() == "x":
                    break
                else:
                    max_i += 50
            paragraph = get_paragraph(hashmap[page], phrase, 0)
            print(f"{i}: Page {page} - {count} occurrences\n{paragraph}\n")
            i += 1
    else:
        print("No results found")


def binary_search(graph, words, hashmap):
    print("Search results:\n")
    result = graph.search_words(words)
    if result:
        sorted_pages = {}
        max_i = 50
        i = 1
        for page, count in sorted_pages:
            if i > max_i:
                choice = input("Press Enter to continue or X to terminate... ")
                if choice.lower() == "x":
                    break
                else:
                    max_i += 50
            paragraph = get_paragraph(hashmap[page], words, 1)
            print(f"{i}: Page {page} - {count} occurrences\n{paragraph}\n")
            i += 1
    else:
        print("No results found")
