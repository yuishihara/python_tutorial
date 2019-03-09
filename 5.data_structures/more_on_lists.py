#!/usr/bin/env python3


def introduction():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    print(fruits.count('apple'))
    print(fruits.count('tangerine'))
    print(fruits.index('banana'))
    print(fruits.index('banana', 4))
    fruits.reverse()
    print(fruits)
    fruits.append('grape')
    print(fruits)
    fruits.sort()
    print(fruits)
    print(fruits.pop())


def using_lists_as_stacks():
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)

    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack)


def using_lists_as_queues():
    from collections import deque

    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")
    queue.append("Graham")
    print(queue.popleft())
    print(queue.popleft())
    print(queue)


def list_comprehensions():
    squares = []
    for x in range(10):
        squares.append(x**2)
    print(squares)

    # side effect caused by above code.
    # You can still use the variable 'x'!!!
    print(x)

    # Alternative approach without side effect
    squares_list_map = list(map(lambda x: x**2, range(10)))
    print(squares_list_map)

    # Equivalent to
    squares_list_comprehension = [x**2 for x in range(10)]
    print(squares_list_comprehension)

    print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

    # Above is (almost) equivalent to
    combs = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                combs.append((x, y))
    print(combs)

    vec = [-4, -2, 0, 2, 4]
    print([x*2 for x in vec])
    print([x for x in vec if x >= 0])
    print([abs(x) for x in vec])

    freshfruit = [' banana', ' loganberry', 'passion fruit']
    print([weapon.strip() for weapon in freshfruit])

    print([(x, x**2) for x in range(6)])
    # This will raise an error
    # [x, x**2 for x in range(6)]

    vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print([num for elem in vec for num in elem])

    from math import pi
    print([str(round(pi, i)) for i in range(1, 6)])


def nested_list_comprehensions():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print([[row[i] for row in matrix] for i in range(4)])

    # This is equivalent to
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])
    print(transposed)

    # And this is also equivalent to
    transposed = []
    for i in range(4):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    print(transposed)

    # And the next is also (almost) equivalent to above

    print(list(zip(*matrix)))


if __name__ == "__main__":
    introduction()
    using_lists_as_stacks()
    using_lists_as_queues()
    list_comprehensions()
    nested_list_comprehensions()
