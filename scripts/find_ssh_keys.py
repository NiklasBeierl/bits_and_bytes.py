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
    size = get_file_size(path)
    with open(path, "rb") as f:
        with file_progress(size) as pbar:
            while f.tell() < size:
                byte = f.read(1)
                if byte == b"B":
                    next = f.read(len(TARGET) - 1)
                    if next == TARGET[1:]:
                        print(hex(f.tell()))
                    else:
                        f.seek(f.tell() - len(TARGET) + 1)
                pbar.set_progress(f.tell())
    print("Done")


def find_keys_or_oom(path: str):
    """
    Bytes are kind of like strings. Or maybe strings are like bytes?
    Also: Lets pretend memory is cheap.
    """
    size = get_file_size(path)
    with open(path, "rb") as f:
        all_bytes = f.read()
    with file_progress(size) as pbar:
        position = -1
        while (position := all_bytes.find(TARGET, position + 1)) != -1:
            print(hex(position))
            pbar.set_progress(position)
        pbar.set_progress(size)
    print("Done")


def find_keys_mmap(path: str):
    """
    But Memory isn't cheap, maybe the OS can help us figure that out?
    """
    with open(path, "rb") as f:
        map = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    size = len(map)
    with file_progress(size) as pbar:
        position = -1
        while (position := map.find(TARGET, position + 1)) != -1:
            print(hex(position))
            pbar.set_progress(position)
        pbar.set_progress(size)
    print("Done")
