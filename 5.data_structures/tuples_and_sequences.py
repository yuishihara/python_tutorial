#!/usr/bin/env python3

if __name__ == "__main__":
    t = 12345, 54321, 'hello!'
    print(t[0])
    print(t)

    u = t, (1, 2, 3, 4, 5)
    print(u)

    # This causes an error. Tuple is immutable!!!
    # t[0] = 88888

    v = ([1, 2, 3], [3, 2, 1])
    print(v)

    # mutable objects inside tuple is still mutable

    v[0][2] = 100
    print(v)

    empty = ()
    singleton = 'hello',
    print(len(empty))
    print(len(singleton))