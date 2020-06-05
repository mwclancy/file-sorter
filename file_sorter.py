from sys import argv
from sys import exit
import os
import shutil

try:
    BASE_PATH = argv[1]
except IndexError:
    print("Error: Path must be passed as argument. Exiting.")
    exit(1)

extensions = []
for i in range(2, len(argv)):
    extensions.append(argv[i])

# create the destination directories if they don't already exist
ext_dict = {}
for ext in extensions:
    path = BASE_PATH + "\\" + ext + "\\"
    path_dir = os.path.dirname(path)
    if not os.path.exists(path_dir):
        print("Creating directory at " + path + "\n")
        os.makedirs(path_dir)
    ext_dict[ext] = path_dir

# iterate trhough the base directory
print("Sorting files......\n")
for dirname, dirnames, filenames in os.walk(BASE_PATH):
    for filename in filenames:
        source = os.path.join(dirname, filename)
        for ext in extensions:
            if filename.upper().endswith(ext.upper()):
                shutil.move(source, os.path.join(ext_dict[ext], filename))
                break

print("Finished.")