from __future__ import print_function
import yaml

# TODO Clear old code, ensure that nothing is behaving badly.

# initialize the yml file to be read
with open('recipes.yaml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

# initialize the variables
infinite = True
result = {}
hex_result = {}


# Get a list of all the colours available
def all_colors():
    color_list = []
    for x in cfg:
        color_list.append(x)
    return color_list


# Deprecated due to GUI
# # Get user input for the colours wanted, ensuring the ability to quit if needed
# def which_color_do_you_want():
#     print("What colour dye are you looking for?")
#     return input().lower()


# Find the color in the ymlfile
def find_color(color):
    for section in cfg:
        if section == color:
            return cfg[section]


# List the colors found, or error if none are found
def color_result(color):
    if find_color(color):
        found = find_color(color)

    # if an item is found, check the ingredients that are either empty or 0 and remove them.
    if found.items():
        for x, y in found.items():
            if y == 0 or y == "":
                continue
            # ensure that the hexcode is a separate entry and isn't added with the ingredients
            if x == "hexcode":
                hex_result[x] = y
                continue
            result[x] = y
        return result, hex_result

# All the following has been deprecated due to GUI.
# # print the required materials as well as the hexcode
# print("\n\nYou need the following materials to make " + color + " dye: \n")
# for x, y in result.items():
#     print(x + ": " + str(y))
# print("\nThis color has the following hexcode: \n")
# for x, y in hex_result.items():
#     print(x + ": " + y)

# # infinitely loop through this program until exited.
# while infinite:
#     coloring = which_color_do_you_want()
#     color_result(coloring)
