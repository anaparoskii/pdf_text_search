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
        if page not in node.pages:
            node.pages.append(page)

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        if node.is_end_of_word:
            return node.pages
        else:
            return None

    def count(self, word, hashmap):
        pages = self.search(word)
        count = []
        for page, text in hashmap.items():
            if page in pages:
                words = text.split()
                for w in words:
                    if word.lower() in w.lower():
                        count.append(page)
        return count

    def build(self, hashmap):
        for page_number, text in hashmap.items():
            words = text.split()
            for word in words:
                self.insert(word.lower(), page_number)
        return self

    def serialize(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def deserialize(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)
