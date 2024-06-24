from color import Color


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

    filtered_pages = []
    for page in pages_with_first_word:
        if page not in pages_with_second_word:
            filtered_pages.append(page)

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


def rank(pages, graph):
    ranked_pages = {}
    for page in pages:
        ranked_pages[page] = ranked_pages.get(page, 0) + 1
    return reference_rank(graph, ranked_pages, 1)


def reference_rank(graph, medium_rank, max_value):
    references = graph.search_references(list(medium_rank.keys()))
    for page_number, reference in references.items():
        if reference in list(medium_rank.keys()):
            medium_rank[reference] *= 1.5
    ranked_pages = sorted(medium_rank.items(), key=lambda item: item[1], reverse=True)
    sorted_pages = []
    for page, frequency in ranked_pages:
        frequency *= max_value
        for page_number, page_references in references.items():
            if page_references in list(medium_rank.keys()):
                medium_rank[page_references] /= 1.5
        sorted_pages.append((page, frequency))
    return sorted_pages


def get_paragraph(page, words, code):
    if code == 1:
        paragraph = page.split('\n')
        paragraph_value = ''
        search_range = len(paragraph) // 2
        for word in words:
            for i in range(search_range, len(paragraph)):
                if word.lower() in paragraph[i].lower():
                    if paragraph_value == '':
                        paragraph_value = paragraph[i]
                    elif paragraph_value == paragraph[i]:
                        continue
                    else:
                        paragraph_value = paragraph_value + '\n' + paragraph[i]
                        break
        for word in words:
            if paragraph_value != '':
                paragraph_value = paragraph_value.lower().replace(word, f"{Color.PURPLE}{word}{Color.RESET}")
        return paragraph_value
    else:
        paragraph = page.split('\n')
        paragraph_value = ''
        search_range = len(paragraph) // 2
        for i in range(search_range, len(paragraph)):
            if words in paragraph[i]:
                if paragraph_value == '':
                    paragraph_value = paragraph[i]
                elif paragraph_value == paragraph[i]:
                    continue
                else:
                    paragraph_value = paragraph_value + '\n' + paragraph[i]
                    break
        if paragraph_value != '':
            paragraph_value = paragraph_value.replace(words, f"{Color.PURPLE}{words}{Color.RESET}")
        return paragraph_value
