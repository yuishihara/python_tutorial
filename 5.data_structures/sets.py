#!/usr/bin/env python3

if __name__ == "__main__":
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)
    print('orange' in basket)
    print('crabgrass' in basket)

    a = set('abracadabra')
    b = set('alacazam')
    print(a)
    print(a - b)
    print(a | b)
    print(a & b)
    print(a ^ b) # a or b but not both

    # set comprehensions
    a = {x for x in 'abracadabra' if x not in 'abc'}
    print(a)