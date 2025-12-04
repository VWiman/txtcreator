from src import PROJECT_ROOT
from src.utils import log
from src.processing import createtxt


def run():
    log(PROJECT_ROOT)
    createtxt()
    return


if __name__ == '__main__':
    run()
