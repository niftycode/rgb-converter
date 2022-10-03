#!/bin/bash

rm -rfv build
rm -rfv dist
pyinstaller main.spec

cd dist
open .

