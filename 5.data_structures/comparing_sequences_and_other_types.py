#!/usr/bin/env python3

if __name__ == "__main__":
    print((1, 2, 3) < (1, 2, 4))
    print([1, 2, 3] < [1, 2, 4])
    print('ABC' < 'C' < 'Pascal' < 'Python')
    print((1, 2, 3, 4) < (1, 2, 4))
    print((1, 2) < (1, 2, -1))
    print((1, 2, 3) == (1.0, 2.0, 3.0))
    print((1, 2, ('aa', 'bb')) == (1, 2, ('abc', 'a'), 4))
