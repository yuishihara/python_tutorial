#!/usr/bin/env python3


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


def class_objects():
    print(MyClass.i)
    print(MyClass.f)
    print(MyClass.f(None))
    x = MyClass()

    class Complex:
        def __init__(self, realpart, imagpart):
            self.r = realpart
            self.i = imagpart

    x = Complex(3.0, -4.5)
    print(x.r, x.i)


def instance_objects():
    x = MyClass()
    x.counter = 1
    while x.counter < 10:
        x.counter = x.counter*2

    print(x.counter)
    del x.counter

    x.counter = 1


def method_objects():
    x = MyClass()
    print(x.f())

    xf = x.f
    print(xf())


def good_designed_class():
    class Dog:
        kind = 'canine'

        def __init__(self, name):
            self.tricks = []
            self.name = name

        def add_trick(self, trick):
            self.tricks.append(trick)

    d = Dog('Fido')
    e = Dog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')
    print('good', d.tricks)
    print('good', e.tricks)


def bad_designed_class():
    class Dog:
        kind = 'canine'
        tricks = []

        def __init__(self, name):
            self.name = name

        def add_trick(self, trick):
            self.tricks.append(trick)
    d = Dog('Fido')
    e = Dog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')
    print('bad', d.tricks)
    print('bad', e.tricks)


def class_and_instance_variables():
    class Dog:
        kind = 'canine'

        def __init__(self, name):
            self.name = name

        def add_trick(self, trick):
            self.tricks.append(trick)

    d = Dog('Fido')
    e = Dog('Buddy')
    print(d.kind)
    print(e.kind)
    print(d.name)
    print(e.name)

    bad_designed_class()
    good_designed_class()

if __name__ == "__main__":
    class_objects()
    instance_objects()
    method_objects()
    class_and_instance_variables()
