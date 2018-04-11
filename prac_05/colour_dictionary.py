COLOUR_HEXADECIMALS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                       "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                       "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                       "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                       "aquamarine4": "#458b74", "azure4": "#838b8b"}
# for state in COLOUR_HEXADECIMALS:
#     print("{:14} is {}".format(state, COLOUR_HEXADECIMALS[state]))
colour = input("What colour hex do you want: ")
if colour in COLOUR_HEXADECIMALS:
    print("The hexadecimal for {} is {}".format(colour, COLOUR_HEXADECIMALS[colour]))
else:
    print("Colour does not exist in dictionary")