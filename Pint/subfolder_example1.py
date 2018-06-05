"""                  
Name: Pint example for use in department files
Department: tutorial
Last updated: 05/06/2018 16:01 by Midas

⚠⚠
WARNING: THIS PROGRAM WILL NOT RUN IN THE CURRENT DIRECTORY! 
         IF YOU WANT TO TEST THIS, COPY PASTE THIS CODE INTO
         YOUR PROGRAM LOCATED IN A SUBFOLDER (LIKE "Aerodynamics") OF
         THE MAIN GITHUB REPOSITORY
⚠⚠ 

DESCRIPTION:
    If you want to use the pint module (for working with units) in another a
    file other then main.py or Aircraft.py, you need to use the format explained
    in this example.
    
"""

import sys
sys.path.append('../') # This makes sure the parent directory gets added to the system path

from Misc import ureg, Q_ # Imports the unit registry fron the Misc folder

## EXAMPLE 1: ASSIGNING A UNIT TO A VALUE

L = 1.234 # Length variable with unassigned unit

print("Before assigning unit:")
print("L =", L) # Print the vaLue of L

L *= ureg.meter # Assign the unit meter to L

print("\nAfter assigning unit:")
print("L =", L) # Print the result

## EXAMPLE 2: CONVERTING UNITS
## This example will convert L
## which is expressed in meters
## to inch

L.ito(ureg.inch) # Convert L to inch
print("\nAfter conversion")
print("L =", L) # print the result

## EXAMPLE 3: GETTING THE MAGNITUDE OF A VALUE
## For compatibility reasons with other software
## You might only want the maginutude of a value
## without the unit, this example shows you how:

L_mag = L.magnitude # Get the magnitude of L
print("\nMagnnitude of L=", L_mag) # Print the result

## EXAMPLE 4: ASSIGING A UNIT USING A STRING EXPRESSION
## You can also assign a value and unit by typing them as a string
## Use Q_(<USER STRING>) function

I_XX = Q_("2457 mm**4") # To have for instance the 4th power, use the python expression **4
I_YY = Q_("0.002 m**4")

print("\n I_XX=", I_XX)
print("I_yy=", I_YY)