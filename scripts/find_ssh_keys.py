import mmap # https://docs.python.org/3/library/mmap.html

from utils import file_progress, get_file_size

TARGET = b"BEGIN OPENSSH PRIVATE KEY"


# We want to find the locations of ssh keys in the memory snapshot.
# In a shell you would simply run:
# strings -t x snap.raw | grep "BEGIN OPENSSH PRIVATE KEY"
# But today we will do it in python. :)


def find_keys_naive(path: str): 
    """
    Lets first do the "naive" thing.
    """
    ...
    print("Done")


def find_keys_or_oom(path: str):
    """
    Bytes are kind of like strings. Or maybe strings are like bytes?
    Also: Lets pretend memory is cheap.
    """
    ...
    print("Done")


def find_keys_mmap(path: str):
    """
    But Memory isn't cheap, maybe the OS can help us figure that out?
    """
    ...
    print("Done")
