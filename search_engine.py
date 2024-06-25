from rank import reference_rank


def search_words(trie, words, graph, hashmap):
    if len(words) >= 3:
        condition = words[1]
        if condition in ["AND", "OR", "NOT"]:
            words = words[0::2]
    else:
        condition = None

    if condition == "AND":
        return and_search(trie, words, hashmap)
    elif condition == "OR":
        return or_search(trie, words, graph, hashmap)
    elif condition == "NOT":
        return not_search(trie, words, hashmap)
    else:
        return default_search(trie, words, graph, hashmap)


def and_search(trie, words, hashmap):
    pages_with_first_word = trie.count(words[0].lower(), hashmap)
    if not pages_with_first_word:
        return []

    pages_with_second_word = trie.count(words[1].lower(), hashmap)
    if not pages_with_second_word:
        return pages_with_first_word

    filtered_pages = []
    for page in pages_with_first_word:
        if page in pages_with_second_word:
            filtered_pages.append(page)
    for page in pages_with_second_word:
        if page in pages_with_first_word:
            filtered_pages.append(page)

    return filtered_pages


def or_search(trie, words, graph, hashmap):
    all_pages = {}
    for word in words:
        pages = trie.count(word.lower(), hashmap)
        if pages:
            all_pages[word] = pages
        else:
            return []
    medium_rank = {}
    i = 0
    while i < 2:
        if i + 1 == 2:
            other = i - 1
        else:
            other = i + 1
        for page in all_pages[words[i]]:
            if page not in all_pages[words[other]]:
                medium_rank[page] = all_pages[words[i]].count(page) / 2
            else:
                medium_rank[page] = (all_pages[words[i]].count(page) + all_pages[words[other]].count(page)) / 2
        i += 1
    return reference_rank(graph, medium_rank, 2)


def not_search(trie, words, hashmap):
    pages_with_first_word = trie.count(words[0].lower(), hashmap)
    if not pages_with_first_word:
        return []

    pages_with_second_word = trie.count(words[1].lower(), hashmap)
    if not pages_with_second_word:
        return pages_with_first_word
    print(pages_with_first_word)
    print(pages_with_second_word)
    filtered_pages = []
    for page in pages_with_first_word:
        if page not in pages_with_second_word:
            filtered_pages.append(page)
    print(filtered_pages)

    return filtered_pages


def default_search(trie, words, graph, hashmap):
    all_pages = {}
    for word in words:
        pages = trie.count(word.lower(), hashmap)
        if pages:
            all_pages[word] = pages
        else:
            return []
    medium_rank = {}
    max_i = len(words)
    for i in range(max_i):
        for page in all_pages[words[i]]:
            count = all_pages[words[i]].count(page)
            for j in range(i + 1, max_i):
                count += all_pages[words[j]].count(page)
            if page not in list(medium_rank.keys()):
                medium_rank[page] = count / max_i
    return reference_rank(graph, medium_rank, max_i)


def search_phrase(phrase, hashmap):
    result = []
    for page, text in hashmap.items():
        lines = text.split("\n")
        for line in lines:
            if phrase in line:
                result.append(page)
    return result
