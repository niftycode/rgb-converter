#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Convert hex value to rgb an vice versa
Version: 1.0
Python 3.10+
Date created: September 18th, 2022
Date modified: -
"""


def hex_to_rgb(hex_value):
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex_value[i:i + 2], 16)
        rgb.append(decimal)

    return tuple(rgb)


def rgb_to_hex(r, g, b):
    return "%02x%02x%02x" % (r, g, b)


def main():
    # rgb_value = hex_to_rgb("FFA501")
    hex_value = rgb_to_hex(255, 165, 1)
    print(hex_value)


if __name__ == '__main__':
    main()
