# -*- coding: utf-8 -*-

# Итератор для удаления дубликатов
class unique(object):
    def __init__(self, items, **kwargs):
        self.iter = len(items)
        self.items = items
        self.ignore_case = kwargs.get('ignore_case')

    def __next__(self):
        if self.ignore_case:
            while len(self.items) > 0:
                item = self.items.pop()
                try:
                    self.items.index(item)
                except ValueError:
                    return item
        else:
            while len(self.items) > 0:
                flag = self.ignore_case
                item = self.items.pop().lower()
                for temp in self.items:
                    if item == temp.lower():
                        flag = False
                        break
                if not flag:
                    return item
        raise StopIteration

        # Нужно реализовать __next__

    def __iter__(self):
        return self
