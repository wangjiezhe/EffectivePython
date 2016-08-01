#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)
print(repr(my_values))


# Use `get` method directly
def main1():
    print('Red:     ', my_values.get('red'))
    print('Green:   ', my_values.get('green'))
    print('Opacity: ', my_values.get('opacity'))


# Add a default value
def main2():
    red = my_values.get('red', [''])[0] or 0
    green = my_values.get('green', [''])[0] or 0
    opacity = my_values.get('opacity', [''])[0] or 0

    print('Red:     %r' % red)
    print('Green:   %r' % green)
    print('Opacity: %r' % opacity)


# Parse as an integer
def main3():
    red = int(my_values.get('red', [''])[0] or 0)

    print('Red:     %r' % red)


# Use `if/else` conditional or ternary expressions
def main4():
    red = my_values.get('red', [''])[0] or 0
    red = int(red[0]) if red[0] else 0

    green = my_values.get('green', [''])
    if green[0]:
        green = int(green[0])
    else:
        green = 0

    print('Red:     %r' % red)
    print('Green:   %r' % green)


# Helper function
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


# Use helper function
def main5():
    green = get_first_int(my_values, 'green')
    print('Green:   %r' % green)


if __name__ == '__main__':
    main1()
    main2()
    main3()
    main4()
    main5()
