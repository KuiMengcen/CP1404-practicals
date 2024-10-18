COLOR_TO_CODE = {"BlueViolet": "#8a2be2", "Bright Green": "#66ff00", "Bisque4": "#8b7d6b", "Bubble Gum": "#ffc1cc",
                 "Chocolate2": "#ee7621", "White": "#ffffff"}
print(COLOR_TO_CODE)
colour_name = input("Enter color name: ").title()
while colour_name != '':
    try:
        print(colour_name, "is", COLOR_TO_CODE[colour_name])
    except KeyError:
        print("Invalid color name")
    colour_name = input("Enter color name: ").title()
