#!/usr/bin/env python3


def reraising():
    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise


if __name__ == "__main__":
    try:
        raise NameError('HiThere')
    except NameError as error:
        print(error)

    try:
        # Shorthand notation
        raise ValueError
    except ValueError as error:
        print(error)

    try:
        reraising()
    except NameError:
        print('Reraised')