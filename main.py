from __future__ import print_function
import yaml

# initialize the yml file to be read
with open('recipes.yaml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

# initialize the variables
infinite = True
result = {}
hex_result = {}
color_list = []


# commented out, I think I have a better way of doing this instead of using command line arguments.
# # check the arguments, if there are any then continue, otherwise list available colours
# if len(sys.argv) >= 2:
#    dye_color_wanted = sys.argv[1]
# else:
#     print("You can search for the following colors:")
#     for x in cfg:
#         color_list.append(x)
#     i = 0
#     while i < len(color_list):
#         if i + 1 == len(cfg):
#             print(color_list[i])
#         else:
#             print(color_list[i], end=", ")
#         i += 1
#     exit()

# Get user input for the colours wanted, ensuring the ability to quit if needed
def which_color_do_you_want():
    print("What colour dye are you looking for?")
    return input().lower()


# Find the color in the ymlfile
def find_color(color):
    for section in cfg:
        if section == color:
            return cfg[section]


# List the colors found, or error if none are found
def color_result(color):
    if find_color(color):
        found = find_color(color)
    elif color == "exit" or "quit" or "q":
        print("\nThanks for coming by!")
        exit()
    else:
        print("\nThis color doesn't exist, sorry.")
        exit()

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

    # print the required materials as well as the hexcode
    print("\n\nYou need the following materials to make " + color + " dye: \n")
    for x, y in result.items():
        print(x + ": " + str(y))
    print("\nThis color has the following hexcode: \n")
    for x, y in hex_result.items():
        print(x + ": " + y)


# infinitely loop through this program until exited.
while infinite:
    coloring = which_color_do_you_want()
    color_result(coloring)
