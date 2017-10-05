"""Check PEP8 and PEP257."""

import subprocess


def codestyle_test(name, first=False, source=True, show_pep8=False, options=False):
    """
    Check PEP8.

    :param name: name of the file
    :param first: adds --first parameter (to show only first occurrence of PEP fail
    :param source: adds --show-source (to show place of the error)
    :param show_pep8: adds --show-pep (to show sourcecode of PEP)
    :param options: adds string with additional options.
    :return: string with style answers
    """
    first = " --first" if first else ""
    source = " --show-source" if source else ""
    show_pep8 = " --show-pep" if show_pep8 else ""
    options = " " + str(options) if options else ""
    command = "pycodestyle{}{}{}{} --max-line-length=120 {}".format(first, source, show_pep8, options, name)
    result = subprocess.run(command, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


def docstyle_test(name, options=False):
    """
    Check PEP257.

    :param name: name of the file
    :param options: adds string with options
    :return: string with style answers
    """
    options = options if options else ""
    command = "pydocstyle{} {}".format(options, name)
    result = subprocess.run(command, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


def main():
    """Initialize program."""
    color_fail = '\033[91m'
    color_end = '\033[0m'
    color_okblue = '\033[94m'

    file = input("Which file do you want to check?: ")
    while "FileNotFoundError: [Errno 2] No such file or directory {}".format(file) in codestyle_test(file):
        print(color_fail + "FileNotFoundError: [Errno 2] No such file or directory: {}".format(file) + color_end)
        print("Try again: ")
        file = input("Which file do you want to check?: ")
    again = "y"
    while "n" not in again.lower():
        print("PEP8 results")
        codestyle = codestyle_test(file)
        if codestyle == "":
            print("All ok!")
        else:
            print(codestyle)
        print("=" * 100)
        print("PEP257 results")
        docstyle = docstyle_test(file)
        if docstyle == "":
            print("All ok!")
        else:
            print(docstyle_test)
        print("=" * 100)
        print(color_okblue + "Hint, save your file before running me again." + color_end)
        again = input("Do you want to run again? (Y/N): ")


if __name__ == "__main__":
    debug = False
    if debug is True:
        print("PEP8 results \n" + codestyle_test("PEPtest.py"))
        print("=" * 100)
        print("PEP257 results \n" + docstyle_test("PEPtest.py"))
    else:
        main()