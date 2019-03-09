#!/usr/bin/env python3

if __name__ == "__main__":
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    print(a)
    del a[0]
    print(a)

    del a[2:4]
    print(a)

    del a[:]
    print(a)
    
    del a
    # Below causes an error since 'a' is no more available
    # print(a)
