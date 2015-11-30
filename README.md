# beatbox_python

# 1. Each of track files suppose to have empty line (or "# notes" line in case of playing notes only).
# 2. Useful function to manage a dictionary:

# writing dict
defs = {'bmp': 120}
f = open('defs.txt','w')
f.write(str(defs))
f.close()

# reading dict
f = open('defs.txt','r')
my_dict = eval(f.read())
my_dict

# 3. enjoy
