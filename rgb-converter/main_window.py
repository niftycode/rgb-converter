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

        # Create a frame
        frame = tk.Frame(self.window, width=600, height=400, bg=BG_COLOR)
        frame.grid(column=0, row=0, sticky="nesw")
        # Prevent the child label element to change the parent frame element
        frame.pack_propagate(False)

        # Load logo image
        logo_img = ImageTk.PhotoImage(file="rgb-converter-logo.png")
        logo_widget = tk.Label(frame, image=logo_img, bg=BG_COLOR)
        logo_widget.image = logo_img
        logo_widget.pack()  # defaults to widget = "top"

        hex_value_label = tk.Label(frame,
                                   text="Enter a hex value: ",
                                    bg=BG_COLOR,
                                    fg="black",
                                    font=("TkMenuFont", 14)
                                    )
        hex_value_label.grid(column=0, row=1)
        hex_value_label.pack()



        def color_change():
            hex_button.configure(bg="red", fg="yellow")

        hex_button = tk.Button(frame, text='click me!', command=color_change())

        hex_text = tk.StringVar()

        # hex_button = tk.Button(frame, textvariable=hex_text, bg=BG_COLOR, font="TkMenuFont")
        hex_text.set("Click me!")
        hex_button.grid(column=1, row=2)
        hex_button.pack()

    def mainloop(self):
        self.window.mainloop()