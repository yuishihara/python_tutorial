#!/usr/bin/env python3

if __name__ == "__main__":
    for i in range(5):
        print(i)
    for i in range(5, 10):
        print(i, end=',')
    print()
    for i in range(0, 10, 3):
        print(i, end=',')
    print()
    for i in range(-10, -100, -30):
        print(i, end=',')
    print()

    # consider using enumerate()
    a = ['Mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(a)):
        print(i, a[i])

    # range does not return a list, returns a iterable instead.
    print(range(10))

    # list creates a list from iterable
    print(list(range(5)))
     