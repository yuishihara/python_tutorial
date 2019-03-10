#!/usr/bin/env python3


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


def simple_exception_handling():
    while True:
        try:
            x = int(input('Please enter a number:'))
            break
        except ValueError:
            print("Oops! That was no valid number. Try again...")


def catching_exceptions():
    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print('D')
        except C:
            print('C')
        except B:
            print('B')


def reraising_exception():
    import sys
    try:
        with open('myfile.txt') as f:
            s = f.readline()
            i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


def else_clause_in_exception():
    import sys
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()


def instantiating_exception():
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)
        x, y = inst.args
        print('x =', x)
        print('y =', y)
        print('x = {0}, y = {1}'.format(*inst.args))


def this_fails():
    x = 1/0


def exception_occurred_in_inner_function():
    try:
        this_fails()
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)


if __name__ == "__main__":
    # simple_exception_handling()
    catching_exceptions()
    reraising_exception()
    else_clause_in_exception()
    instantiating_exception()
    exception_occurred_in_inner_function()
