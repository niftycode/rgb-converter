#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Convert hex value to rgb an vice versa
Version: 1.0
Python 3.10+
Date created: September 22th, 2022
Date modified: -
"""

import tkinter as tk

from PIL import ImageTk

BG_COLOR = "#D3F7EC"


class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("RGB Converter")
        self.window.eval("tk::PlaceWindow . center")

        self.frame = tk.Frame(self.window, width=600, height=400, bg=BG_COLOR)
        self.frame.grid(row=0, column=0, sticky="nesw")

    def mainloop(self):
        self.window.mainloop()