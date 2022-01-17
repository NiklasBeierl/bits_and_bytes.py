import argparse
from importlib import import_module

from memory_profiler import memory_usage


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("module")

    parser.add_argument("func")
    parser.add_argument("func_args", nargs="*")
    args = parser.parse_args()

    mod_name = args.module.removesuffix(".py")
    module = import_module(mod_name)
    func = getattr(module, args.func)
    usage = memory_usage((func, tuple(args.func_args)))
    print(f"Peak memory usage: {max(usage):.2f} MiB")


if __name__ == "__main__":
    main()
