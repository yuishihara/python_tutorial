#!/usr/bin/env python3

def clean_up():
    try:
        raise KeyboardInterrupt
    finally:
        print('Goodbye, world!')


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


if __name__ == "__main__":
    # clean_up()

    divide(2, 1)
    divide(2, 0)
    divide("2", "1")
