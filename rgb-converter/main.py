#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Convert hex value to rgb an vice versa
Version: 1.0
Python 3.9+
Date created: September 18th, 2022
Date modified: September 23rd, 2022
"""

import logging

import main_window

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


BG_COLOR = "#D3F7EC"


def main():
    app_instance = main_window.MainWindow()
    app_instance.mainloop()


if __name__ == '__main__':
    main()
