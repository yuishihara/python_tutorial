#!/usr/bin/env python


def f1(self, x, y):
    return min(x, x+y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


def f2(self, x, y):
    return max(x, x+y)


def function_defined_outside_the_class():
    x = C()

    print(x.f(2, 1))

    C.e = f2
    y = C()

    print(x.e(2, 1))
    print(y.e(2, 1))


def call_method_from_another():
    class Bag:
        def __init__(self):
            self.data = []

        def add(self, x):
            self.data.append(x)

        def addtwice(self, x):
            self.add(x)
            self.add(x)

    bag = Bag()
    bag.add('red bag')
    bag.addtwice('blue bag')

    print(bag.data)


if __name__ == "__main__":
    function_defined_outside_the_class()
    call_method_from_another()
