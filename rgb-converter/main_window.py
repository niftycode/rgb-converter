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

from PIL import ImageTk

BG_COLOR = "#D3F7EC"


class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("RGB Converter")
        # self.window.iconbitmap('./assets/pythontutorial.ico')

        # Set width and height of the window
        window_width = 600
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
        self.window.columnconfigure(1, weight=3)

        # Load logo image
        logo_img = ImageTk.PhotoImage(file="assets/rgb-converter-logo.png")
        logo_widget = ttk.Label(self.window, image=logo_img)
        logo_widget.image = logo_img
        logo_widget.grid(columnspan=2, column=0, row=0)

        hex_label = ttk.Label(self.window,
                              text="Enter a hex value",
                              font=("Helvetica", 20))
        hex_label.grid(column=0, row=1, pady=20)

        rgb_label = ttk.Label(self.window,
                              text="Enter rgb values",
                              font=("Helvetica", 20))
        rgb_label.grid(column=0, row=2, pady=20)

        hex_text = tk.StringVar()
        hex_textbox = ttk.Entry(self.window, textvariable=hex_text)
        hex_textbox.grid(column=1, row=1)

        # text_content = text.get('1.0','end')
        # Create an Exit button.
        # b2 = Button(win, text="Exit", command=win.destroy)

        '''

        hex_button = tk.Button(frame,
                               text='click me!',
                               bg="green",
                               height=3,
                               width=5
                               )

        hex_text = tk.StringVar()
        hex_text.set("Click me!")
        hex_button.grid(column=1, row=2)
        hex_button.pack()
    '''

    def mainloop(self):
        self.window.mainloop()
