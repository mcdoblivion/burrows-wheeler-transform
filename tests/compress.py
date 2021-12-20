import sys, os, subprocess
import traceback

from core.__main__ import *
from os.path import isfile, join

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

tests_dir = os.getcwd() + "/"

try:
    txt_files = [tests_dir + f for f in os.listdir(tests_dir) if isfile(join(tests_dir, f))]
    txt_files = filter(lambda x: x[-4:] == ".txt", txt_files)

    for i in txt_files:
        print("Compressing file " + i)
        compress(i)
except Exception as e:
    print(e)
    traceback.print_exc()
