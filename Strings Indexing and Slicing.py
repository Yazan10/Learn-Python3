# __________________________
# String Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object contain Elements
# [3] Every Element Has OWn Index
# [4] Python use zero Based Indexing (Index Start From Zero)
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuple or lists
# __________________________

# Indexing (Access Single Item)

myString="i love python"
print(myString[0]) # Index 0 => I
print(myString[1]) # Index 1 => Space ( )
print(myString[2]) # Index 2 => l
print(myString[-1]) # Index -1 => First Character From End
print(myString[-6]) # Index -6 => 6th Character From End

# Slicing ( Access Muliple Elements Squance Item )
# [Start:End] End Not Included
# [Start:End:Steps]
print(myString[8:11]) # yth
print(myString[3:5]) # ov

print(myString[:11]) # If start is not Here Will Start From 0 (I love pyth)
print(myString[5:]) # If end is not Here Will Go To The End (I love pyt)
print(myString[:]) # Full Data
print(myString[0::1]) # Full Data
print(myString[::1]) # Full Data
print(myString[::2]) # ilv yhn
print(myString[::3]) # io tn