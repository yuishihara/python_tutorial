#!/usr/bin/env python

if __name__ == "__main__":
    string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
    non_null = string1 or string2 or string3
    print(non_null)