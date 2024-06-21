from color import Color


def rank(result):
    ranked_pages = {}
    for page in result:
        for i in page:
            if i in list(ranked_pages.keys()):
                ranked_pages[i] += 1
            else:
                ranked_pages[i] = 1
    return ranked_pages


def search_result(result):
    ranked_pages = rank(result)
    sorted_pages = sorted(ranked_pages.items(), key=lambda x: x[1], reverse=True)
    return sorted_pages


def get_paragraph(page, words):
    paragraph = page.split('\n')
    paragraph_value = ''
    for word in words:
        for i in range(len(paragraph)//2, len(paragraph)):
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
            paragraph_value = paragraph_value.replace(word, f"{Color.PURPLE}{word}{Color.RESET}")
    return paragraph_value
