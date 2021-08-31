"""
Create a program that allows you to look up hexadecimal colour codes
"""

COLOUR_CODES = {"aliceblue": "#f0f8ff", "black": "#000000", "blueviolet": "#8a2be2", "cadetblue": "#5f9ea0",
                "chocolate": "#d2691e", "coral": "#ff7f50", "cornflowerblue": "#6495ed", "darkorange": "#ff8c00",
                "deeppink1": "#ff1493", "firebrick1": "#ff3030"}

print(COLOUR_CODES)

colour_name = input("Colour: ").lower()
while colour_name != "":
    print(f"The code for '{colour_name}' is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Colour: ").lower()
print("Have a nice day :)")
