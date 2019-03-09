#!/usr/bin/env python3

if __name__ == "__main__":
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))

    # Don't do below to avoid infinite loop
    # for w in words:
    # instead do
    for w in words[:]:
        if len(w) > 6:
            words.insert(0, w)
    print(words)