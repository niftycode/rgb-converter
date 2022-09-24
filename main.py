#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Convert hex value to rgb an vice versa
Version: 1.0
Python 3.9+
Date created: September 18th, 2022
Date modified: September 23rd, 2022
"""


from rgb_converter import main_window


BG_COLOR = "#D3F7EC"


def main():
    app_instance = main_window.MainWindow()
    app_instance.mainloop()


if __name__ == '__main__':
    main()
