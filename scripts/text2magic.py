#!/usr/bin/python3

import os.path

debug = 1
path = "lib/font-sky130/"

text = """MawsonLakes.Org - Google + Skywater 130nm Shuttle
Date: November 2020
Version: 1

The SKY130 is a mature 180nm-130nm hybrid technology originally
developed internally by Cypress Semiconductor before being spun out
into SkyWater Technology and made accessible to general industry.
SkyWater and Google's collaboration is now making this technology
accessible to everyone!
"""

copyright = """© Paul Schulz <paul@mawsonlakes.org>"""

characters = """ !"#$%&'()*+,-./
0123456789:;<=>?
@ABCDEFGHIJKLMNO
PQRSTUVWXYZ[/]^_
`abcdefghijklmno
pqrstuvwxyz{|}~
©
😀
"""

# Configuration
print("path: ", path)

#for a in text:
#    print('{:s} 0x{:02x}'.format(a,ord(a)))

for ch in characters:
    ch_ord = ord(ch)

    # Handle whitespace
    if (ch == "\n" or ch == "\t"):
        ch = ' ';

    if (ord(ch) < 0x100):
        filename = "font_{:02X}.mag".format(ord(ch))
    elif (ord(ch) < 0x10000):
        filename = "font_{:04X}.mag".format(ord(ch))
    elif (ord(ch) < 0x1000000):
        filename = "font_{:06X}.mag".format(ord(ch))
    else:
        filename = "font_{:X}.mag".format(ord(ch))

    msg = ""
    if (os.path.isfile(path+filename)):
        msg = msg+"*** Exists "

    print('{:s} 0x{:02X} {}'.format(ch, ord(ch), msg))
