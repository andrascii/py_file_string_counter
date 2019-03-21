import sys
import argparse
from os import listdir
from os.path import isfile, join, splitext


def file_len(filename):
    with open(filename, errors="ignore") as f:
        for i, l in enumerate(f):
            pass
        return i + 1
    return 0


def get_all_files(path, extensions, excluded_dirs=[]):
    all_files = []
    all_subdirectories = []

    try:
        for f in listdir(path):
            full_path = join(path, f)
            is_file = isfile(full_path)
            _, file_extension = splitext(full_path)

            if is_file and file_extension.strip(".") in extensions:
                all_files.append(full_path)

            elif not is_file and f not in excluded_dirs:
                all_subdirectories.append(full_path)

    except FileNotFoundError:
        print("Unexpected error")

    for subdir in all_subdirectories:
        all_files += get_all_files(subdir, extensions)

    return all_files


def get_params():
    path = ""
    searching_extensions = []
    excluded_dirs = []

    if len(sys.argv) == 1:
        print("Enter the path to the source codes: ", end="")
        path = input()

        print("Enter the list of target file extensions to count (split them using space): ", end="")
        extensions_list_str = input()
        searching_extensions = extensions_list_str.split(" ")

        print("Enter the list directories to exclude from searching (split them using space): ", end="")
        exclude_dirs_list_str = input()
        excluded_dirs = exclude_dirs_list_str.split(" ")

    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("--path", type=str)
        parser.add_argument("--ext", type=str)
        parser.add_argument("--exdirs", type=str)
        args = parser.parse_args(sys.argv)
        print(args)

    return path, searching_extensions, excluded_dirs


def main():
    program_params = get_params()
    all_target_files = get_all_files(program_params[0], program_params[1], program_params[2])

    print(*all_target_files, sep="\n")
    print("Found", len(all_target_files), "files")

    string_count = 0

    for f in all_target_files:
        string_count += file_len(f)

    print("String count in all files:", string_count)


if __name__ == "__main__":
    main()
