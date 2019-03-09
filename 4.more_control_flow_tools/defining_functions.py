#!/usr/bin/env python3


def fib(n):  # write Fibonacci series up to n
    """This first line is a docstring"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    fib(2000)

    f = fib
    f(100)

    # functions return None in case no return statement exist
    print(fib(0))

    f100 = fib2(100)
    print(f100)
