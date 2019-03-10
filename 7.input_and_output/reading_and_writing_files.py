#!/usr/bin/env python3
import os


def introduction():
    f = open('workfile', 'w')
    print(f.closed)
    f.close()
    print(f.closed)

    with open('workfile') as f:
        print(f.closed)
    print(f.closed)
    os.remove('workfile')


def methods_of_file_objects():
    with open('file1', 'w') as f:
        f.write('This is the entire file.\n')

    with open('file1') as f:
        print(repr(f.read()))
        print(repr(f.read()))
    os.remove('file1')

    with open('file2', 'w') as f:
        f.write('This is the first line of the file.\n')
        f.write('Second line of the file.\n')

    with open('file2') as f:
        print(repr(f.readline()))
        print(repr(f.readline()))

    with open('file2') as f:
        for line in f:
            print(line, end='')
    os.remove('file2')

    with open('file3', 'w') as f:
        size = f.write('This is a test\n')
        print(size)
    os.remove('file3')

    with open('file4', 'w') as f:
        value = ('the answer', 42)
        s = str(value)  # tuple -> string
        print(f.write(s))
    os.remove('file4')

    with open('workfile', 'wb+') as f:
        print(f.write(b'0123456789abcdef'))
        # index starts from 0. This, 5 means 6th byte
        print(f.seek(5))
        print(repr(f.read(1)))
        # second arg 2 means end of file
        print(f.seek(-3, 2))
        print(repr(f.read(1)))
    os.remove('workfile')


def saving_structured_data_with_json():
    import json
    print(json.dumps([1, 'simple', 'list']))

    with open('jsonfile', 'w+') as f:
        x = [1, 'simple', 'list']
        print(x)
        json.dump(x, f)

        f.seek(0)
        x = json.load(f)
        print(x)
    os.remove('jsonfile')

if __name__ == "__main__":
    introduction()
    methods_of_file_objects()
    saving_structured_data_with_json()
