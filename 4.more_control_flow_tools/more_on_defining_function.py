#!/usr/bin/env python3


def ask_ok(prompt, retries=4, reminder='Please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


def check_default_arg_evaluation_timing():
    # Check that default arg is evaluated and set at first time when function is defined
    i = 5

    def f(arg=i):
        print(arg)

    i = 6

    # Should print 5
    f()


def default_arg_is_mutable():
    def f(a, L=[]):
        L.append(a)
        return L

    print(f(1))
    print(f(2))
    print(f(3))


def avoid_sharing_default_arg():
    def f(a, L=None):
        if L is None:
            L = []
        L.append(a)
        return L

    print(f(1))
    print(f(2))
    print(f(3))


def default_argument_values():
    # Uncomment below to check function argument usage
    # ask_ok('Do you really want to quit?')
    # ask_ok('OK to overwrite the file?', 2)
    # ask_ok('OK to overwrite the file?', 'Come on, only yes or no!')

    check_default_arg_evaluation_timing()
    default_arg_is_mutable()
    avoid_sharing_default_arg()


def keyword_arguments():
    def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it")
        print("-- Lovely plumage, the", type)
        print("-- It's", state, "!")

    parrot(1000)
    parrot(voltage=1000)
    parrot(voltage=1000000, action='VOOOOOM')
    parrot(action='VOOOOOM', voltage=1000000)
    parrot('a million', 'bereft of life', 'jump')
    parrot('a thousand', state='pushing up the daisies')

    # invalid calls
    # parrot()
    # parrot(voltage=5.0, 'dead')
    # parrot(110, voltage=220)
    # parrot(actor='John Cleese')

    def function(a):
        pass

    # This is also invalid
    # function(0, a=0)
    def cheeseshop(kind, *arguments, **keywords):
        print("-- Do you have any", kind, "?")
        print("-- I'm sorry, we're all out of", kind)
        for arg in arguments:
            print(arg)
        print("-" * 40)
        for kw in keywords:
            print(kw, ":", keywords[kw])

    cheeseshop('Limburger', "It's very runny, sir",
               "It's really very, VERY runny, sir",
               shopkeeper="Michael Palin",
               client="John Cleese",
               sketch="Cheese Shop Sketch")


def arbitrary_argument_lists():
    def concat(*args, sep="/"):
        return sep.join(args)
    print(concat("earth", "mars", "venus"))
    print(concat("earth", "mars", "venus", sep="."))


def unpacking_argument_lists():
    print(list(range(3, 6)))
    args = [3, 6]
    print(list(range(*args)))

    def parrot(voltage, state='a stiff', action='voom'):
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.", end=' ')
        print("E's", state, "!")

    d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
    parrot(**d)


def lambda_expressions():
    def make_incrementor(n):
        return lambda x: x + n

    f = make_incrementor(42)
    print(f(0))
    print(f(1))

    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1])
    print(pairs)


def documentation_strings():
    def my_function():
        """Do nothing, but document it.
        No, really, it doesn't do anything.
        """

    print(my_function.__doc__)


def function_annotations():
    def f(ham: str, eggs: str = 'eggs') -> str:
        print("Annotations:", f.__annotations__)
        print("Arguments:", ham, eggs)
        return ham + ' and ' + eggs

    print(f('spam'))


if __name__ == "__main__":
    default_argument_values()
    keyword_arguments()
    arbitrary_argument_lists()
    unpacking_argument_lists()
    lambda_expressions()
    documentation_strings()
    function_annotations()
