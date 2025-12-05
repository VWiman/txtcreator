from src import DATA_DIR
from src.utils import log
from os import walk

# Create a .txt file for each image file (with the same name) in directory and write the filename to it
def createtxt():
    filenames = next(walk(DATA_DIR), (None, None, []))[2]
    exeptions = set()
    for i in filenames:
        filename = str(i)[:-4]
        try:
            f = open(f'dataset/{filename}.txt', "x")
            f.write(filename)
            log(f'Created dataset/{filename}.txt')
        except FileExistsError:
            if filename not in exeptions:
                log(f'Failed to create dataset/{filename}.txt as it already exists.')
                exeptions.add(filename)
