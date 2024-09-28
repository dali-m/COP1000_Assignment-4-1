"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
# Number of characters.
# Color of characters.
# Type of wood.
charge=35.00
numChars=8
color="gold"
woodType="oak"

numChars=int(input("Enter number of characters: "))
woodType=str(input("Enter wood type: "))
color=str(input("Enter color: "))


# Write assignment and if statements here as appropriate.
if numChars > 5:
    charge = charge + (numChars-5)*4

if woodType=="oak":
    charge = charge + 20

if color == "gold":
    charge = charge + 15
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))

