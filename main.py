"""Check PEP8 and PEP257."""

import subprocess

try:
    from setup import BASEPATH
except ImportError:
    BASEPATH = ""


def codestyle(path, first=False, source=True, show_pep8=False, options=False):
    """
    Check PEP8.

    :param path: name of the file
    :param first: adds --first parameter (to show only first occurrence of PEP fail
    :param source: adds --show-source (to show place of the error)
    :param show_pep8: adds --show-pep (to show sourcecode of PEP)
    :param options: adds string with additional options.
    :return: string with style answers
    """
    path = BASEPATH + path
    first = "--first" if first else ""
    source = "--show-source" if source else ""
    show_pep8 = "--show-pep" if show_pep8 else ""
    options = str(options) if isinstance(options, str) else ""
    options = " {} {} {} {}  --max-line-length=120".format(first, source, show_pep8, options)
    command = "pycodestyle{} {}".format(options, path)
    result = subprocess.run(command, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


def docstyle(path, options=False):
    """
    Check PEP257.

    :param path: name of the file
    :param options: adds string with options
    :return: string with style answers
    """
    path = BASEPATH + path
    options = options if isinstance(options, str) else ""
    command = "pydocstyle {} {}".format(options, path)
    result = subprocess.run(command, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


def main():
    """Initialize program."""
    color_fail = '\033[91m'
    color_end = '\033[0m'
    color_okblue = '\033[94m'
    color_warnning = '\033[93m'
    if BASEPATH == "":
        print(color_warnning + "BASEPATH not set, you can set it in setup.py" + color_end)
    print("Which file do you want to check?(insert path): ")
    file = input(BASEPATH)

    file_not_found = "FileNotFoundError: [Errno 2] No such file or directory:"
    while file_not_found in codestyle(file):
        print(color_fail + "FileNotFoundError: [Errno 2] No such file or directory" + color_end)
        print("Try again: ")
        if BASEPATH == "":
            print(color_okblue + "Hint, you should enter path ex:'C:/my/path/to/file.py'." + color_end)
            print("Which file do you want to check?(insert path): ")
        else:
            print("Which file do you want to check?(insert path): ")
        file = input(BASEPATH)

    again = "y"
    while "n" not in again.lower():
        print("PEP8 results")
        output_style = codestyle(file)
        if output_style == "":
            print("All ok!")
        else:
            print(output_style)
        print("=" * 100)
        print("PEP257 results")
        output_doc = docstyle(file)
        if output_doc == "":
            print("All ok!")
        else:
            print(output_doc)
        print("=" * 100)
        print(color_okblue + "Hint, save your file before running me again." + color_end)
        again = input("Do you want to run again? (Y/N): ")


if __name__ == "__main__":
    debug = False
    if debug is True:
        print("PEP8 results \n" + codestyle("PEPtest.py"))
        print("=" * 100)
        print("PEP257 results \n" + docstyle("PEPtest.py"))
    else:
        main()
