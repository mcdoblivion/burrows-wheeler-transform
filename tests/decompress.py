import sys, os, subprocess
from core.__main__ import *

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    h_files = subprocess.check_output('ls tests/*.h', shell=True).split()
    for i in h_files:
        print("Decompressing file " + i + "..")
        decompress(i)
except Exception as e:
    print("No .h files available to decompress")
