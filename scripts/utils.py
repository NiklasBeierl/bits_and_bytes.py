from pathlib import Path

from tqdm import tqdm


def get_file_size(path: str) -> int:
    return Path(path).stat().st_size


class file_progress(tqdm):
    """
    Progress bar for linearly processing a file, configured for acceptable overhead despite many iterations.
    Use like so:
    >>> with file_progress(get_file_size(path)) as pbar:
            for offset in ... # Somehow iterate over the file
                # Do something inside your loop
                pbar.set_progress(offset) # Set to the offset in the file you are working with in this iteration
    """
    def __init__(self, size: int, *args, **kwargs):
        super().__init__(
            *args,
            total=size,
            unit_divisor=1024,
            unit_scale=True,
            unit="B",
            # Tames the overhead introduced by the progress bar
            maxinterval=3.0,
            miniters=1000,
            **kwargs
        )

    def set_progress(self, prog: int):
        self.update(prog - self.n)

    def set_description(self, *args, **kwargs):
        # Refresh set to false to avoid overhead.
        super().set_description(*args, refresh=False, **kwargs)
