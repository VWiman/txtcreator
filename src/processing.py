from src import DATA_DIR
from os import walk


def createtxt():
    filenames = next(walk(DATA_DIR), (None, None, []))[2]
    print(filenames)