'''
COLOR_TO_HEX = {
    "AliceBlue": #F0F8FF,
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "#00FFFF",
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF",
    "Beige": "#F5F5DC",
    "Bisque": "#FFE4C4",
    "Black": "#000000",
    "BlanchedAlmond": "#FFEBCD",
    "Blue": "#0000FF"
}

print(COLOR_TO_HEX)

get color name
while color_name is not blank
    if color_name in COLOR_TO_HEX
        print(f"The hexadecimal code for {color_name} is {COLOR_TO_HEX[color_name]}")
    else
        print Invalid message
    get color name
'''
COLOR_TO_HEX = {
    "AliceBlue": "#F0F8FF",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "#00FFFF",
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF",
    "Beige": "#F5F5DC",
    "Bisque": "#FFE4C4",
    "Black": "#000000",
    "BlanchedAlmond": "#FFEBCD",
    "Blue": "#0000FF"
}

print(COLOR_TO_HEX)

color_name = input("Enter a color name: ").strip().title()
while color_name != "":
    if color_name in COLOR_TO_HEX:
        print(f"The hexadecimal code for {color_name} is {COLOR_TO_HEX[color_name]}")
    else:
        print("Invalid color name")
    color_name = input("Enter a color name: ").strip().title()