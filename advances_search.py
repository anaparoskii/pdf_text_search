from stack import Stack
import re
from rank import rank
from paragraph import print_result


def advanced_search(expression, trie, hashmap, graph):
    stack = Stack()
    tokens = tokenize(expression)
    expression_words = []
    word_list = []
    for token in tokens:
        if token == "(" or token in ["AND", "OR", "NOT"]:
            stack.push(token)
        elif token == ")":
            while stack.top() != "(":
                word_list.append(stack.pop())
            stack.pop()
        else:
            word_list.append(token)
    while not stack.is_empty():
        word_list.append(stack.pop())

    for word in word_list:
        if word not in ["AND", "OR", "NOT"]:
            expression_words.append(word)
            stack.push(trie.count(word.lower(), hashmap))
        else:
            second = stack.pop()
            first = stack.pop()
            stack.push(advanced_operations(first, second, word))

    result = stack.pop()
    if len(result) > 0:
        sorted_pages = rank(result, graph)
        print_result(sorted_pages, hashmap, expression_words, 1)
    else:
        print("No results found")


def advanced_operations(list1, list2, operation):
    return_value = []
    if operation == "AND":
        for page in list1:
            if page in list2:
                return_value.append(page)
        for page in list2:
            if page in list1:
                return_value.append(page)
    elif operation == "OR":
        return_value = list1 + list2
    elif operation == "NOT":
        for page in list1:
            if page not in list2:
                return_value.append(page)
    return return_value


def tokenize(expression):
    pattern = r'\(|\)|AND|OR|NOT|\b\w+\b'
    return re.findall(pattern, expression)
