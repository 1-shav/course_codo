import sys
from os import path

def path_correction_somethinf(relative_path):
    base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
    return path.abspath(path.join(base_path, relative_path))

path_correction_somethinf("logooo.png")