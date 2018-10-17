"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os
import shutil


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    #Attempt to enter lyrics subdirectory, if fails create new subdirectory
    try:
        os.chdir('Lyrics')
    except FileExistsError:
        os.mkdir('Lyrics')
        os.chdir('Lyrics')
    #Display the folder name for each folder inside the lyrics folder
    for foldername in os.listdir('.'):

        if os.path.isdir(foldername):
            print("Files in {}:\n{}\n".format(os.getcwd(), foldername))

    #Create an example temp folder inside the Lyrics folder
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    #Print the file names in each subdirectory of Lyrics
    for foldername in os.listdir('.'):

        if os.path.isdir(foldername):
            os.chdir(foldername)
            for filename in os.listdir('.'):

                if os.path.isdir(filename):
                    continue

                new_name = get_fixed_filename(filename)
                os.rename(filename, new_name)

                print("Renaming {} to {}".format(filename, new_name))
            os.chdir("../")
    #Shutil.move example
    #Create Dummy File
    open("Dummy.txt", 'a').close()
    shutil.move("Dummy.txt", "temp/Dummy.txt")
    os.chdir("../")
    demo_walk()

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    try:
        os.chdir('Lyrics')
    except FileExistsError:
        os.mkdir('Lyrics')
        os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            song_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(song_name, new_name)


main()