import struct  # https://docs.python.org/3/library/struct.html
import mmap  # https://docs.python.org/3/library/mmap.html
import re  # https://docs.python.org/3/library/re.html
import numpy as np  # https://numpy.org/

from utils import file_progress, get_file_size


# Pointers in x86 are stored as "aligned" little endian 8 byte unsigned integers
POINTER_SIZE = 8
POINTER_FORMAT = "<Q"  # https://docs.python.org/3/library/struct.html#format-strings


# "Kernel space" pointers in x86 have bits [63:47] set to 1
KPOINTER_MASK = (2 ** 17 - 1) << 47


def find_kpointers_naive(path: str):
    """
    Lets first do the "naive" thing.
    """
    size = get_file_size(path)
    pointers = []
    ...
    print(f"Done, found: {len(pointers)} kernel pointers.")


def find_kpointers_mmap(path: str):
    """
    Maybe the OS can help us speed this up a little.
    """
    pointers = []
    ...
    print(f"Done, found: {len(pointers)} kernel pointers.")


KPOINTER_PATTERN = re.compile(...)


def find_kpointers_regex(path: str):
    """
    Regex on bytes? Sure, why not?
    """
    ...
    print(f"Done, found: {len(pointers)} kernel pointers.")


def find_kpointers_numpy(path: str):
    """
    The fastest way to loop in python is not to loop in python. - mCoding
    # https://www.youtube.com/watch?v=Qgevy75co8c
    """
    ...
    print(f"Done, found: {len(pointers)} kernel pointers.")


if __name__ == "__main__":
    find_kpointers_numpy("../data/snap.raw")
