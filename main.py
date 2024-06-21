from parse_pdf import parse_pdf
from graph import Graph
from search_engine import search_result, get_paragraph


def main():
    print("------ TEXT SEARCH ------")
    hashmap = parse_pdf()
    graph = Graph()
    graph = graph.build(hashmap)
    while True:
        print("""
            [x] Exit
            [0] Search for words in the text
            """)
        choice = input("Enter choice: ")
        if choice == "x":
            break
        elif choice == "0":
            value = input("Enter words to search for in the text: ")
            words = value.split()
            if value[0] == "'" or value[0] == '"':
                phrase = value[1:-1]
                result = graph.search_phrase(phrase, hashmap)
            else:
                result = graph.search_words(words)
            print("Search results:\n")
            if result:
                sorted_pages = search_result(result)
                i = 1
                for page, count in sorted_pages:
                    if value[0] == "'" or value[0] == '"':
                        paragraph = get_paragraph(hashmap[page], value[1:-1], 0)
                    else:
                        paragraph = get_paragraph(hashmap[page], words, 1)
                    print(f"{i}: Page {page} - {count} occurrences\n{paragraph}\n")
                    i += 1
            else:
                print("No results found")
        else:
            print("Invalid choice")
    print("------ END ------")


if __name__ == "__main__":
    main()
