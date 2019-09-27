#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""FS_TUI

Copyright (c) 2018-2019 by André Perron.  All rights reserved.
https://github.com/binaryguru/cross2rekordbox_xml

MIT License

Copyright (c) 2019 André Perron

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import sys
import argparse as AP

# Commandline argument parsing
PARSER = AP.ArgumentParser(prog='cross2rekordbox_xml',
                           description='Tool to fix beatgrid offsets in'
                           'rekordbox.xml exported by Mixvibes Cross.')
PARSER.add_argument('-d', '--dump', action='store_true',
                    help='Dump fixed XML to standard output instead of file')
PARSER.add_argument('-v', '--verbose', action='store_true',
                    help='Display a list of items fixed in the output file')
PARSER.add_argument('-D', '--debug', action='store_true',
                    help='Enable debug mode')
ARGS = PARSER.parse_args()

print('FS_TUI')
exit()
