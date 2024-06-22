from parse_pdf import parse_pdf
from graph import Graph
from search_mode import words_search, phrase_search, binary_search


def main():
    print("------ TEXT SEARCH ------")
    hashmap = parse_pdf()
    graph = Graph()
    graph = graph.deserialize('serialization/graph.pkl')
    while True:
        print("""
            You can search word(s) or phrases in the text 
            You search phrases by enclosing them in single or double quotes
            You search words by separating them with spaces
            You can use binary search by typing words and separating them with keywords AND, OR, NOT
            
            [X] Exit
            [0] Search for words in the text
            """)
        choice = input("Enter choice: ")
        if choice.lower() == "x":
            break
        elif choice == "0":
            value = input("Enter words to search for in the text: ")
            words = value.split()
            if value[0] == "'" or value[0] == '"':
                phrase = value[1:-1]
                phrase_search(graph, phrase, hashmap)
            elif len(words) > 1 and words[1] in ["AND", "OR", "NOT"]:
                binary_search(graph, words, hashmap)
            else:
                words_search(graph, words, hashmap)
        else:
            print("Invalid choice")
    graph.serialize('serialization/graph.pkl')
    print("------ END ------")


if __name__ == "__main__":
    main()
