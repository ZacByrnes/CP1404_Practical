"""
CP1404/CP5632 Practical - Suggested Solution
Hexadecimal colour lookup
"""

COLOR_NAMES_AND_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                         "AntiqueWhite1": "#ffefdb", "brown1": "#ff4040", "chartreuse1":
                         "#7fff00", "aquamarine2": "#76eec6",
                         "coral": "#ff7f50", "CornflowerBlue": "	#6495ed",
                         "beige": "#f5f5dc", "DarkOrchid": "	#9932cc"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOR_NAMES_AND_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")
