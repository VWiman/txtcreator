from src import DATA_DIR
from os import walk

# Create a .txt file for each image file (with the same name) in directory and write the filename to it
def createtxt():
    filenames = next(walk(DATA_DIR), (None, None, []))[2]
    for i in filenames:
        filename = str(i)[:-4]
        f = open(f'dataset/{filename}.txt', "x")
        f.write(filename)
        print(filename)
    print(filenames)