"""
    mode='r'  read only
    mode='w'  overwrite or create new file if not found
    mode='a'  append
    mode='r+' r+w
    mode='w+' w+r overwrites or create new
"""
with open("myfile.txt", mode="r+") as my_new_file:
    contents = my_new_file.read()

with open("myfile.txt", mode="a") as f:
    f.write("\nFour on fourth")

