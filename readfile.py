#!/usr/bin/python
'''Doc-string
this does something, but I really don't know what.
Well I kind of do now.  But need to play around more
with pythons docstring functions.
'''

# Open a file
fo = open("README.md", "r+")
str = fo.read(10)
print ("Read String is : ", str)

# Check current position
position = fo.tell()
print  ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(200)
print ("Again read String is : ", str)
# Close opend file
fo.close()
