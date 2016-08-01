#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main1():
    # The `else` block will run
    for i in range(3):
        print('Loop %d' % i)
    else:
        print('Else block!')

    # The `else` block won't run
    for i in range(3):
        print('Loop %d' % i)
        if i == 1:
            break
    else:
        print('Else block!')

    # The `else` block will run immediately if you loop over an empty sequence
    for _ in []:
        print('Never runs')
    else:
        print('For Else block!')

    # also when `while` loops are initially false
    while False:
        print('Never runs')
    else:
        print('While Else block!')


# Use `else` block when using loops to search for something
def main2():
    a = 4
    b = 9

    for i in range(2, min(a, b) + 1):
        print('Testing,', i)
        if a % i == 0 and b % i == 0:
            print('Not coprime')
            break
    else:
        print('Coprime')


# Return early when you find the condition you're looking for
def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        print('Testing,', i)
        if a % i == 0 and b % i == 0:
            return False
    return True


# Use a result variable that indicates whether you've found what you're looking for in the loop
def coprime2(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        print('Testing,', i)
        if a % i == 0 and b % i == 0:
            is_coprime = False
    return is_coprime


if __name__ == '__main__':
    main1()
    main2()
