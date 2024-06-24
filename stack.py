class EmptyStackError(Exception):
    pass


class Stack(object):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty!")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty!")
        return self._data[-1]
