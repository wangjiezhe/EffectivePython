#!/usr/bin/env python
# -*- coding: utf-8 -*-

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']

for flavor in flavor_list:
    print('%s is delicious' % flavor)

# Use `range`
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i + 1, flavor))

# Use `enumerate`
for i, flavor in enumerate(flavor_list):
    print('%d: %s', (i + 1, flavor))

# Counting from 1 instead of 0
for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s', (i, flavor))
