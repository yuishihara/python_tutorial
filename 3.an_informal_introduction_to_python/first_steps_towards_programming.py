#!/usr/bin/env python3

if __name__ == "__main__":
    a, b = 0, 1
    while a < 10:
        print(a)
        a, b = b, a+b

    i = 256 * 256
    print('The value of i is', i)

    a, b = 0, 1
    while a < 1000:
        print(a, end=',')
        a, b = b, a+b
