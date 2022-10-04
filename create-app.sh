#!/bin/bash

rm -rfv build
rm -rfv dist
# pyinstaller main.spec
pyinstaller RGB-Converter.spec
# pyinstaller --onefile --windowed --icon icon.icns --name testApp main.py
# pyinstaller -w --debug=all --onefile --windowed --name RGB-Converter rgb_converter/main_window.py

cd dist
open .

