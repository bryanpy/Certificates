from os import walk

filenames = next(walk("Zenva"), (None, None, []))[2]
print(filenames)