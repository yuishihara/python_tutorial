#!/usr/bin/env python3

if __name__ == "__main__":
    a = (i*i for i in range(10)) # this is not a tuple, is a generator
    print(a)
    print(sum(a))

    xvec = [10, 20, 30]
    yvec = [7, 5, 3]
    print(sum(x*y for x,y in zip(xvec, yvec)))

    from math import pi, sin

    sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
    print(sine_table)
    page = ['hello', 'world', 'hello', 'world2']
    unique_words = set(word for line in page for word in line.split())
    print(unique_words)

    data = 'golf'
    print(list(data[i] for i in range(len(data)-1, -1, -1)))