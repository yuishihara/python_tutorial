#!/usr/bin/env python3


def numbers():
    print(2+2)
    print(50 - 5*6)
    print((50 - 5*6) / 4)
    print(8 / 5)
    print(17 / 3)
    print(17 // 3)
    print(17 % 3)
    print(5 * 3 + 2)
    print(5 ** 2)
    print(2 ** 7)
    width = 20
    height = 5 * 9
    print(width * height)

    # Uncomment below to check python raising error
    # print(n)

    print(4 * 3.75 - 1)


def strings():
    print('spam eggs')
    print('doesn\'t')
    print("doesn't")
    print('"Yes," they said.')
    print('"Isn\'t," they said.')
    s = 'First line.\nSecond line.'
    print(s)
    print('C:\some\name')
    print(r'C:\some\name')
    # concatenate with next line using \
    print("""\
Usage: thingy [OPTIONS]
-h Display this usage message
-H hostname Hostname to connect to
""")
    print(3 * 'un' + 'ium')
    print('Py''thon')
    text = ('Put several strings within parenthesis '
            'to have them joined together.')
    print(text)

    prefix = 'Py'
    # uncomment below to check python raising error
    # prefix 'thon'
    print(prefix + 'thon')

    word = 'Python'
    print(word[0])
    print(word[5])
    print(word[-1])
    print(word[-2])
    print(word[-6])

    print(word[0:2])
    print(word[2:5])

    print(word[:2] + word[2:])
    print(word[:4] + word[4:])

    print(word[:2])
    print(word[4:])
    print(word[-2:])

    # How slicing works
    # +---+---+---+---+---+---+
    # | P | y | t | h | o | n |
    # +---+---+---+---+---+---+
    # 0   1   2   3   4   5   6
    #-6  -5  -4  -3  -2  -1

    # print(word[42]) this is out of range
    print(word[4:42])
    print(word[42:])

    # uncomment below to check python raising error
    # word[0] = 'J'
    # word[2:] = 'py'

    print('J' + word[1:])
    print(word[:2] + 'py')

    s = 'supercalifragilisticexpialidocious'
    print(len(s))


def lists():
    squares = [1, 4, 9, 16, 25]
    print(squares)
    print(squares[0])
    print(squares[-1])
    print(squares[-3:])
    print(squares[:])
    print(squares + [36, 49, 64, 81, 100])

    cubes = [1, 8, 27, 65, 125]  # cubes[3] is wrong
    print(cubes)
    print(4**3)
    cubes[3] = 64
    print(cubes)
    cubes.append(216)
    cubes.append(7 ** 3)
    print(cubes)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters)
    letters[2:5] = ['C', 'D', 'E']
    print(letters)
    letters[2:5] = []
    print(letters)
    letters[:] = []
    print(letters)

    letters = ['a', 'b', 'c', 'd']
    print(len(letters))

    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]
    print(x)
    print(x[0])
    print(x[0][1])


if __name__ == "__main__":
    numbers()
    strings()
    lists()
