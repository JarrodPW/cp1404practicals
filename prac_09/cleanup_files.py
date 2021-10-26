"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # Handle Title Case with spaces e.g., Away In A Manger
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""
    for i, char in enumerate(filename):
        # Handle Sentence Case with no spaces or brackets
        if char.islower() and (filename[i - 1] == "_" or filename[i - 1] == "("):
            new_name += char.upper()
        else:
            new_name += char
        # Handle PascalCase e.g., SilentNight
        try:
            if char.isalpha() and filename[i + 1].isupper():
                new_name += '_'
        except IndexError:
            pass
    return new_name


def run_tests():
    filenames = ['SilentNight.txt', 'Away In A Manger.txt', 'ItIsWell (oh my soul).txt',
                 'O little town of bethlehem.TXT']
    for filename in filenames:
        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


main()
# run_tests()
