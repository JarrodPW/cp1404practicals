"""
Do-from-scratch Exercise - prac 09
"""
import os
import shutil


def main():
    """Create directories for each new extension and move the correlating files into the respective directory."""
    print(os.getcwd())

    os.chdir('FilesToSort')

    print(os.getcwd())

    print(os.listdir('.'))

    for filename in os.listdir('.'):
        directory = filename.split('.')[-1]
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass
        shutil.move(filename, directory)

        print(f"{directory}/{filename}")


main()
