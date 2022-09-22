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

from tkinter import ttk  # import newer widgets
from tkinter import messagebox
from PIL import ImageTk

import converter


BG_COLOR = "#D3F7EC"


class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("RGB Converter")
        # self.window.iconbitmap('./assets/pythontutorial.ico')

        # Set width and height of the window
        window_width = 700
        window_height = 400

        # Get the screen dimension
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # Set the position of the window to the center of the screen
        self.window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        # Window is not resizable
        self.window.resizable(False, False)

        # Configure the grid
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.columnconfigure(3, weight=1)
        self.window.columnconfigure(4, weight=1)

        # Load logo image
        logo_img = ImageTk.PhotoImage(file="assets/rgb-converter-logo.png")
        logo_widget = ttk.Label(self.window, image=logo_img)
        logo_widget.image = logo_img
        logo_widget.grid(columnspan=5, column=0, row=0)

        # Load labels
        hex_label = ttk.Label(self.window,
                              text="Enter hex value:",
                              font=("Helvetica", 16))
        hex_label.grid(column=0, row=1, pady=4, sticky="w")

        rgb_label = ttk.Label(self.window,
                              text="Enter RGB values:",
                              font=("Helvetica", 16))
        rgb_label.grid(column=0, row=2, pady=4, sticky="w")

        output_label = ttk.Label(self.window,
                                 text="Result:",
                                 font=("Helvetica", 16))
        output_label.grid(column=0, row=3, pady=15, sticky="w")

        result_label = ttk.Label(self.window,
                                 text="",
                                 font=("Helvetica", 16))
        result_label.grid(column=1, columnspan=2, row=3, pady=15, sticky="w")

        # Load entries
        hex_text = tk.StringVar()
        hex_textbox = ttk.Entry(self.window, textvariable=hex_text, width=6)
        hex_textbox.grid(column=1, row=1, sticky="w")

        r_text = tk.StringVar()
        r_textbox = ttk.Entry(self.window, textvariable=r_text, width=4)
        r_textbox.grid(column=1, row=2, sticky="w")

        g_text = tk.StringVar()
        g_textbox = ttk.Entry(self.window, textvariable=g_text, width=4)
        g_textbox.grid(column=2, row=2, sticky="w")

        b_text = tk.StringVar()
        b_textbox = ttk.Entry(self.window, textvariable=b_text, width=4)
        b_textbox.grid(column=3, row=2, sticky="w")

        exit_button = tk.Button(self.window,
                                text="Exit",
                                width=6,
                                command=self.window.destroy)
        exit_button.grid(column=0, row=4, sticky="w")

        def _show_rgb_values():
            user_input = hex_text.get()
            result = converter.hex_to_rgb(user_input)
            result_label.config(text=result)

        def _show_hex_value():
            r_input = int(r_text.get())
            g_input = int(g_text.get())
            b_input = int(b_text.get())

            result = converter.rgb_to_hex(r_input, g_input, b_input)
            result_label.config(text=result)

        # Load buttons
        hex_button = tk.Button(self.window,
                               text="Show RGB values",
                               height=1,
                               width=10,
                               command=_show_rgb_values
                               )
        hex_button.grid(column=4, row=1)

        rgb_button = tk.Button(self.window,
                               text="Show hex value",
                               height=1,
                               width=10,
                               command=_show_hex_value
                               )
        rgb_button.grid(column=4, row=2)


    def mainloop(self):
        self.window.mainloop()
