#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value  # Instance of unicode


def to_str(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value  # Instance of str


if __name__ == '__main__':
    print(to_unicode('abc'))
    print(to_unicode(u'aβc'))
    print(to_str('abc'))
    print(to_str(u'aβc'))
