#!/usr/bin/env python


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update


class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)


if __name__ == "__main__":
    base = Mapping(['hello', 'world'])
    print(base.items_list)

    sub = MappingSubclass(['hello', 'world'])
    print(sub.items_list)
    
    sub.update(['key1', 'key2'], ['hello', 'world'])
    print(sub.items_list)
