fname = raw_input("neter the file name")
with open(fname) as f:
    content = f.readlines()

print content[0]