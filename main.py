from __future__ import print_function
import yaml
import sys

with open('recipes.yaml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

result = {}
hex_result = {}
color_list = []

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    print("You can search for the following colors:")
    for x in cfg:
        color_list.append(x)
    i = 0
    while i < len(color_list):
        if i + 1 == len(cfg):
            print(color_list[i])
        else:
            print(color_list[i], end=", ")
        i += 1
    exit()


def find_color(color):
    for section in cfg:
        if section == color:
            return cfg[section]


def color_result(color):
    if find_color(color):
        found = find_color(color)
    else:
        print("This color doesn't exist, sorry.")
        exit(0)

    if found.items():
        for x, y in found.items():
            if y == 0 or y == "":
                continue
            if x == "hexcode":
                hex_result[x] = y
                continue
            result[x] = y

    print("You need the following materials to make this color dye: \n")
    for x, y in result.items():
        print(x + ": " + str(y))
    print("\nThis color has the following hexcode: \n")
    for x, y in hex_result.items():
        print(x + ": " + y)


color_result(filename)
