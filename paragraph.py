from color import Color


def print_result(sorted_pages, hashmap, words, code):
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
        paragraph = get_paragraph(hashmap[page], words, code)
        count = round(count)
        print(f"{i}: Page {page} - {count} occurrences\n{paragraph}\n")
        i += 1


def get_paragraph(page, words, code):
    if code == 1:
        paragraph = page.split('\n')
        paragraph_value = ''
        max_words_found = 0
        for row in paragraph:
            word_count = 0
            for word in words:
                if word.lower() in row.lower():
                    word_count += 1
            if word_count > max_words_found:
                max_words_found = word_count
                paragraph_value = row
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
