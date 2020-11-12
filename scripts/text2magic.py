#!/usr/bin/python3

import os.path
import pprint

debug = 0
path = "libraries/sky130_pschulz_xx_hd/mag/"
# scale = 2

text = """MawsonLakes.Org - Google + Skywater 130nm Shuttle
Date: November 2020
Version: 1

The SKY130 is a mature 180nm-130nm hybrid technology originally
developed internally by Cypress Semiconductor before being spun out
into SkyWater Technology and made accessible to general industry.
SkyWater and Google's collaboration is now making this technology
accessible to everyone!
"""

copyright = """© Paul Schulz <paul@mawsonlakes.org>
License: Apache License Version 2.0"""

characters = """ !"#$%&'()*+,-./
0123456789:;<=>?
@ABCDEFGHIJKLMNO
PQRSTUVWXYZ[/]^_
`abcdefghijklmno
pqrstuvwxyz{|}~
©
😀
"""

def get_cell_name (ch):
    """Return name of cell used to store character data"""

    if (ord(ch) < 0x100):
        cellname = "font_{:02X}".format(ord(ch))
    elif (ord(ch) < 0x10000):
        cellname = "font_{:04X}".format(ord(ch))
    elif (ord(ch) < 0x1000000):
        cellname = "font_{:06X}".format(ord(ch))
    else:
        cellname = "font_{:X}".format(ord(ch))

    return cellname

def get_file_name(cellname):
    filename = get_cell_name(cellname)+".mag"
    return filename

# Test
def font_status (string):
    """Check characters in string"""
    for ch in characters:
        ch_ord = ord(ch)

        # Handle whitespace
        if (ch == "\n" or ch == "\t"):
            ch = ' ';

        filename = get_file_name(ch)
        msg = filename
        if (os.path.isfile(path+filename)):
            msg = msg+" *** Exists "

        print('  {:s} 0x{:02X} {}'.format(ch, ord(ch), msg))

##############################################################################
def read_character_cell (character):
    """Read character details from file"""
    filename = get_file_name(character)
    file1 = open(path+filename, 'r')
    Lines = file1.readlines()

    count = 0
    mode = "top"
    data = {}
    for line in Lines:
        line = line.strip()
        count = count+1
        linedata = line.split()

        if debug:
            print("Line{}: {}".format(count, line))

        if linedata[0] =="<<":
            if linedata[1] == "metal1":
                mode = "metal1"
            if linedata[1] == "properties":
                mode = "properties"
            if linedata[1] == "end":
                mode = "end"

        if mode == "top":
            if linedata[0] == "magic":
                data["filetype"] = "magic"
            elif linedata[0] == "tech":
                data["tech"] = linedata[1]
            elif linedata[0] == "timestamp":
                data["timestamp"] = linedata[1]

        if mode == "metal1":
            if linedata[0] == "rect":
                if "left" in data:
                    if int(linedata[1]) < data["left"]:
                        data["left"] = int(linedata[1])
                else:
                    data["left"] = int(linedata[1])

                if "right" in data:
                    if int(linedata[3]) > data["right"]:
                        data["right"] = int(linedata[3])
                else:
                    data["right"] = int(linedata[3])

                if "bottom" in data:
                    if int(linedata[2]) < data["bottom"]:
                        data["bottom"] = int(linedata[2])
                else:
                    data["bottom"] = int(linedata[2])

                if "top" in data:
                    if int(linedata[4]) < data["top"]:
                        data["top"] = int(linedata[4])
                else:
                    data["top"] = int(linedata[4])

        if mode == "properties":
           if linedata[0] == "string" and linedata[1] == "FIXED_BBOX":
               data["FIXED_BBOX"] = [linedata[2],linedata[3],linedata[4],linedata[5]]

    # Calculate bounding box size
    if "FIXED_BBOX" in data:
        data["bbox-width"]  = int(data["FIXED_BBOX"][2]) - int(data["FIXED_BBOX"][0])
        data["bbox-height"] = int(data["FIXED_BBOX"][3]) - int(data["FIXED_BBOX"][1])
    else:
        data["bbox-width"]  = data["right"] - data["left"]
        data["bbox-height"] = data["top"] - data["bottom"]

    # Calculate character skip
    # If bounding box present, use that (regular character with FIXED_BBOX)
    # otherwise use furthest paint (something without a bounding box)
    # else zero skip,
    if "FIXED_BBOX" in data:
        data["skip"] = int(data["FIXED_BBOX"][2])
    elif "right" in data:
        data["skip"] = data["right"]
    else:
        data["skip"] = 0
    data["skip"] = data["skip"]*2
    return data

def print_cell_data (data):
    """Display the cell data stored in 'data'"""
    print(data)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)

def write_character (character,metrics):
    """Write a character, and use character metrics to move to cursor to next
character location.
    """
    print("# "+character)
    print("pushbox")
    print("getcell "+get_cell_name(character)+" child 0 0")
    print("popbox")
    print("box move r "+str(metrics["skip"]))
    print()

def write_text (message):
    x = 0
    y = 0
    baselineskip = 1200
    metrics = {}

    print("box position {} {}".format(x,y))
    print()

    for char in message:
        if char != "\n":
            metrics[char] = read_character_cell(char)
            write_character(char,metrics[char])
        else:
            x = 0
            y = y - baselineskip
            print("box position {} {}".format(x,y))
            print()

##############################################################################
# Configuration
# print("path: ", path)

# Test
# font_status(characters)

# for a in text:
#    print('{:s} 0x{:02x}'.format(a,ord(a)))

write_text("Test...!!?")
