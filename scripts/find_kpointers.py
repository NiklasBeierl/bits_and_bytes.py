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
    with open(path, "rb") as f:
        with file_progress(size) as pbar:
            while f.tell() < size:
                word = f.read(POINTER_SIZE)
                as_int = struct.unpack(POINTER_FORMAT, word)[0]
                # as_int = int.from_bytes(word, "little") # Alternatively
                if (as_int & KPOINTER_MASK) == KPOINTER_MASK:
                    pointers.append(f.tell())
                    pbar.set_description(f"Found {len(pointers)} kpointers.")
                pbar.set_progress(f.tell())

    print(f"Done, found: {len(pointers)} kernel pointers.")


def find_kpointers_mmap(path: str):
    """
    Maybe the OS can help us speed this up a little.
    """
    pointers = []
    with open(path, "rb") as f:
        memap = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    with file_progress(len(memap)) as pbar:
        for i in range(0, len(memap), 8):
            word = memap[i : i + POINTER_SIZE]
            as_int = struct.unpack(POINTER_FORMAT, word)[0]
            pbar.set_progress(i)
            if (as_int & KPOINTER_MASK) == KPOINTER_MASK:
                pointers.append(i)
                pbar.set_description(f"Found {len(pointers)} kpointers.")

    print(f"Done, found: {len(pointers)} kernel pointers.")


KPOINTER_PATTERN = re.compile(b"(?=(.{5}[\x80-\xFF]\xFF\xFF))", flags=re.DOTALL)
# Wrapped in a lookahead to catch "overlapping matches"
# Consider:
# 00 01 02 03 04 05 06 07  10 11 12 13 FF FF FF FF
# 00 01 02 03 04 05 06(07  10 11 12 13 FF FF FF)FF   <- 1. Match
# 00 01 02 03 04 05 06 07 (10 11 12 13 FF FF FF FF)  <- 2. Match (ignored by regex)
# Without the "lookahead trick" we will only get the first!


def find_kpointers_regex(path: str):
    """
    Regex on bytes? Sure, why not?
    """
    pointers = []
    with open(path, "rb") as f:
        memap = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    with file_progress(len(memap)) as pbar:
        for match in KPOINTER_PATTERN.finditer(memap): # type: ignore
            offset = match.start()
            pointers.append(offset)
            if offset % POINTER_SIZE == 0:
                pbar.set_description(f"Found {len(pointers)} kpointers.")
                pbar.set_progress(offset)

    print(f"Done, found: {len(pointers)} kernel pointers.")


def find_kpointers_numpy(path: str):
    """
    The fastest way to loop in python is not to loop in python. - mCoding
    # https://www.youtube.com/watch?v=Qgevy75co8c
    """
    with open(path, "rb") as f:
        memap = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    npmap = np.memmap(path, dtype=np.uint64)
    is_pointer = np.bitwise_and(npmap, KPOINTER_MASK) == KPOINTER_MASK
    pointers = is_pointer.nonzero()[0]

    print(f"Done, found: {len(pointers)} kernel pointers.")


if __name__ == "__main__":
    find_kpointers_numpy("../data/snap.raw")
