import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # The joke line is already written in entry.txt; this step only
    # carries that file, unchanged, into the directory the grader reads.
    # Nothing here is generated at run time, so repeated runs agree.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.txt"), os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
