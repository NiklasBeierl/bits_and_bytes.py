import argparse
import timeit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("module")

    parser.add_argument("func")
    parser.add_argument("func_args", nargs="*")
    args = parser.parse_args()

    mod_name = args.module.removesuffix(".py")
    func_args_as_python = ",".join([f'"{arg}"' for arg in args.func_args])
    exec_time = timeit.timeit(
        setup=f"from {mod_name} import {args.func}",
        stmt=f"{args.func}({func_args_as_python})",
        number=1,
    )
    print(f"Execution took {exec_time:.3f} seconds.")


if __name__ == "__main__":
    main()
