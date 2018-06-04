# -*- coding: utf-8 -*-
"""
This is an example program on how to use the "pint" Unit calculation tool.
For more info, see https://computationalmodelling.bitbucket.io/tools/Pint.html

Created on Mon Jun  4 16:42:21 2018
@author: midas
"""

### NOTE: MAKE SURE THE PINT MODULE IS INSTALLED ON YOUR PC
###       RUN "pip install pint" in the command prompt to install the module

from pint import UnitRegistry

unit = UnitRegistry() # Initialise the unit module

## EXAMPLE 1: ASSIGNING A UNIT TO A VALUE

L = 1.234 # Length variable with unassigned unit

print("Before assigning unit:")
print("L =", L) # Print the vaLue of L

L *= unit.meter # Assign the unit meter to L

print("\nAfter assigning unit:")
print("L =", L) # Print the result

## EXAMPLE 2: CONVERTING UNITS
## This example will convert L
## which is expressed in meters
## to inch

L.ito(unit.inch) # Convert L to inch
print("\nAfter conversion")
print("L =", L) # print the result

## EXAMPLE 3: GETTING THE MAGNITUDE OF A VALUE
## For compatibility reasons with other software
## You might only want the maginutude of a value
## without the unit, this example shows you how:

L_mag = L.magnitude # Get the magnitude of L
print("\nMagnnitude of L=", L_mag) # Print the result