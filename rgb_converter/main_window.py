#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Convert hex value to rgb an vice versa
Version: 1.0
Python 3.9+
Date created: September 22th, 2022
Date modified: September 24th, 2022
"""

import tkinter as tk

from tkinter import ttk  # import newer widgets
# from PIL import ImageTk

from rgb_converter import converter


BG_COLOR = "#D3F7EC"


class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("RGB Converter")
        # self.window.iconbitmap('./assets/pythontutorial.ico')

        # Set width and height of the window
        window_width = 500
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

        # Load logo image
        # logo_img = ImageTk.PhotoImage(file="rgb_converter/assets/rgb-converter-logo.png")
        # logo_widget = ttk.Label(self.window, image=logo_img)
        # logo_widget.image = logo_img
        # logo_widget.grid()

        ttk.Label(
            self.window,
            text="RGB Converter",
            font=("TkDefaultFont", 20)
        ).grid()

        # Create Widgets in a Frame (mf = main frame)
        # to keep geometry management simpler
        mf = ttk.Frame(self.window)
        mf.grid(padx=20, sticky=(tk.E + tk.W))
        mf.columnconfigure(0, weight=1)

        # Input Frame (Hex & RGB values)
        input_frame = ttk.LabelFrame(mf, text="Input")
        input_frame.grid(sticky=(tk.W + tk.E))
        for i in range(2):
            input_frame.columnconfigure(i, weight=1)

        # Hex Label & Entry (row 1)
        hex_label = ttk.Label(input_frame,
                              text="Enter hex value:",
                              font=("Helvetica", 14))
        hex_label.grid(column=0, row=1, sticky=tk.W)

        hex_text = tk.StringVar()
        hex_textbox = ttk.Entry(input_frame, textvariable=hex_text, width=6)
        hex_textbox.grid(column=1, row=1, sticky=(tk.W + tk.E))

        # Hex button
        hex_button = tk.Button(input_frame,
                               text="Show RGB values",
                               height=1,
                               width=10,
                               command=_show_rgb_values
                               )
        hex_button.grid(column=4, row=1)

        # RGB Labels & Entries (row 2)
        rgb_label = ttk.Label(input_frame,
                              text="Enter RGB values:",
                              font=("Helvetica", 14))
        rgb_label.grid(column=0, row=2, sticky=tk.W)

        r_text = tk.StringVar()
        r_textbox = ttk.Entry(input_frame, textvariable=r_text, width=6)
        r_textbox.grid(column=1, row=2, sticky=(tk.W + tk.E))

        g_text = tk.StringVar()
        g_textbox = ttk.Entry(input_frame, textvariable=g_text, width=6)
        g_textbox.grid(column=2, row=2, sticky=(tk.W + tk.E))

        b_text = tk.StringVar()
        b_textbox = ttk.Entry(input_frame, textvariable=b_text, width=6)
        b_textbox.grid(column=3, row=2, sticky=(tk.W + tk.E))

        # RGB button
        rgb_button = tk.Button(input_frame,
                               text="Show hex value",
                               height=1,
                               width=10,
                               command=_show_hex_value
                               )
        rgb_button.grid(column=4, row=2)

        # Output Frame
        output_frame = ttk.LabelFrame(mf, text="Output")
        output_frame.grid(pady=40, sticky=(tk.W + tk.E))
        for i in range(2):
            input_frame.columnconfigure(i, weight=1)

        output_label = ttk.Label(output_frame,
                                 text="Result:",
                                 font=("Helvetica", 14))
        output_label.grid(column=0, row=1, pady=15, sticky="w")

        result_label = ttk.Label(output_frame,
                                 text="",
                                 font=("Helvetica", 14))
        result_label.grid(column=1, row=1, sticky="w")

        exit_button = tk.Button(mf,
                                text="Exit",
                                width=6,
                                command=self.window.destroy)
        exit_button.grid(sticky=tk.E)

    def mainloop(self):
        self.window.mainloop()
