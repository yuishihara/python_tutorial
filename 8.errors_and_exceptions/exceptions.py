#!/usr/bin/env python3


def print_error(error):
    print(str(error), 'occurred')


if __name__ == "__main__":
    try:
        10 * (1/0)
        # should not reach here
        assert False
    except ZeroDivisionError as error:
        print_error(error)

    try:
        4 + spam * 3
        # should not reach here
        assert False
    except NameError as error:
        print_error(error)

    try:
        '2' + 2
        # should not reach here
        assert False
    except TypeError as error:
        print_error(error)
