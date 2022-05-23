import os

dirname = os.path.dirname


def py2ui(fpath):
    dirSRC = dirname(dirname(__file__))
    return os.path.join(dirSRC, "ui", os.path.split(fpath)[1][:-3] + ".ui")