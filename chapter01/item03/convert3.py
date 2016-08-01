#!/usr/bin/env python
# -*- coding: utf-8 -*-


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes


if __name__ == '__main__':
    print(to_str('aβc'))
    print(to_str(b'abc'))
    print(to_bytes('aβc'))
    print(to_bytes(b'abc'))
