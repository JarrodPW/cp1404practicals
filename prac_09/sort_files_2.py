"""
Do-from-scratch Exercise - prac 09
"""
import os
import shutil


def main():
    """Create directories for each new extension and move the correlating files into the respective directory."""
    extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input(f"What category would you like to sort {extension} files into? ").title()
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, f"{extension_to_category[extension]}/{filename}")


main()















