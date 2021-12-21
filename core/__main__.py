#!/usr/bin/python
import sys
import time
import os
import bwt
import huffman
import mtf


def record_time(f):
    def w(*a):
        start = time.time()
        f(*a)
        stop = time.time()
        print("Completed in %f s" % (stop - start))

    return w


@record_time
def compress(filename):
    bwt.encode_file(filename, filename + ".bwt")
    mtf.encode_file(filename + ".bwt")
    huffman.compress(filename + ".bwt.mtf", filename + ".bwt.mtf.bin")


@record_time
def decompress(filename):
    huffman.decompress(filename, filename.replace(".bin", ""))
    mtf.decode_file(filename.replace(".bin", ""))
    bwt.decode_file(filename.replace(".mtf.bin", ""), filename.replace(".bwt.mtf.bin", ".decoded"))


@record_time
def huffman_compress(filename):
    huffman.compress(filename, filename + ".bin")


@record_time
def huffman_decompress(filename):
    huffman.decompress(filename, filename.replace(".bin", ""))


@record_time
def bwt_huffman_compress(filename):
    bwt.encode_file(filename, filename + ".bwt")
    huffman.compress(filename + ".bwt", filename + ".bwt.bin")


# compress("../tests/test.txt")
# decompress("../tests/test.txt.bwt.mtf.bin")

# huffman_compress("../tests/test.txt")
# bwt_huffman_compress("../tests/test.txt")
