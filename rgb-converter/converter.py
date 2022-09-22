#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Convert hex value to rgb an vice versa
This file contains the converter methods:
- hex_to_rgb()
- rgb_to_hex

Version: 1.0
Python 3.10+
Date created: September 22th, 2022
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
