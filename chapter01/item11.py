#!/usr/bin/env python
# -*- coding: utf-8 -*-

names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]


# Use iteration
def main1():
    longest_name = None
    max_letters = 0

    for i in range(len(names)):
        count = letters[i]
        if count > max_letters:
            longest_name = names[i]
            max_letters = count

    print(longest_name)


# Use `enumerate`
def main2():
    longest_name = None
    max_letters = 0

    for i, name in enumerate(names):
        count = letters[i]
        if count > max_letters:
            longest_name = name
            max_letters = count

    print(longest_name)


# Use `zip`
def main3():
    longest_name = None
    max_letters = 0

    for name, count in zip(names, letters):
        if count > max_letters:
            longest_name = name
            max_letters = count

    print(longest_name)


if __name__ == '__main__':
    main1()
    main2()
    main3()
