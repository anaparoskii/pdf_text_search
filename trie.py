import pickle


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.pages = []


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, page):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.pages.append(page)

    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        if node.is_end_of_word:
            return node.pages
        else:
            return None

    @staticmethod
    def build(hashmap):
        trie = Trie()
        for page_number, text in hashmap.items():
            words = text.split()  # Split text into words (simplified)
            for word in words:
                trie.insert(word.lower(), page_number)
        return trie

    def serialize(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def deserialize(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)
