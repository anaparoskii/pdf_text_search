import pickle
import re


class Graph(object):
    def __init__(self):
        self.data = {}

    def add_edge(self, node, edge):
        if self.has_node(node):
            self.data[node].append(edge)
        else:
            self.data[node] = [edge]

    def has_node(self, node):
        return node in self.data

    def search_page_references(self, node):
        if self.has_node(node):
            return self.data[node]
        return None

    def search_pages_references(self, pages):
        references = {}
        for node in pages:
            if self.has_node(node):
                references[node] = self.data[node]
        return references

    @staticmethod
    def get_references(text):
        references = []
        pattern = r'page\s+(\d+)'
        matches = re.findall(pattern, text)
        for match in matches:
            references.append(int(match) + 22)
        return references

    def build(self, hashmap):
        for page_number, text in hashmap.items():
            references = self.get_references(text)
            if references:
                for ref in references:
                    self.add_edge(page_number, ref)
            else:
                self.add_edge(page_number, None)
        return self

    def serialize(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def deserialize(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)
