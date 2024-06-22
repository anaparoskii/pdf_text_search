import pickle


class Graph(object):
    def __init__(self):
        self.data = {}

    def add_edge(self, node, edge):
        if node in self.data:
            self.data[node].append(edge)
        else:
            self.data[node] = [edge]

    def get_pages(self, node):
        return self.data.get(node, [])  # returns list of pages

    def has_node(self, node):
        return node in self.data

    def __str__(self):
        return str(self.data)

    def search_word(self, word):
        word = word.lower()
        if self.has_node(word):
            return self.get_pages(word)
        return None

    def search_words(self, words):
        result = []
        for word in words:
            result.append(self.search_word(word))
        return result

    @staticmethod
    def search_phrase(phrase, hashmap):
        result = []
        for page, text in hashmap.items():
            lines = text.split("\n")
            for line in lines:
                if phrase in line:
                    result.append(page)
        return result

    def build(self, dictionary):
        for page_number, text in dictionary.items():
            words = text.split()
            for word in words:
                self.add_edge(word.lower(), page_number)
        return self

    def serialize(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def deserialize(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)
