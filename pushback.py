# An iterator which allows to "unget" the items returned from it.
# If some value was pushed back, the next call to `__next__` will return
# this value.
class PushBackIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.added_elements = []

    def __iter__(self):
        return self

    def __next__(self):
        while self.added_elements:
            return self.added_elements.pop()
        return next(self.iterator)

    def push_back(self, element):
        self.added_elements.append(element)

    def has_next(self):
        if self.added_elements:
            return True
        try:
            self.push_back(next(self.iterator))
            return True
        except StopIteration:
            return False
