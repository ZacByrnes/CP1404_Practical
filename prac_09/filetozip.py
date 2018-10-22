"""open("Dummy.txt", 'a').close()
    shutil.move("Dummy.txt", "temp/Dummy.txt")
    os.chdir("../")
    """
import os
import shutil

def main():
    extension_list = [""]
    os.chdir('FilesToSort')
    #Find all possible extensions in folder
    folder_contents = os.listdir()
    print(*folder_contents, sep = ",")
    for folder_content in folder_contents:
        print('1')
        if os.path.isfile(folder_content):
            folder_content_parts = folder_content.split('.')
            extension = folder_content_parts[len(folder_content_parts) - 1]
            print(folder_content)
            print(extension + "\\" + folder_content)
            #Checks all different parts to get the extension e.g if there was 4 it would take 1 to get extension
            print('2')
            if (extension not in extension_list):
                extension_list.append(extension)
                #Create the subdirectories
                print('5')
                try:
                    print('6')
                    os.mkdir(extension)
                except FileExistsError:
                    print('7')
                    pass
            print('3')
                    #No further action is required
            #Move all files into respective extension subdirectories
            try:
                print(folder_content)
                print(extension + "\\" + folder_content)
                shutil.move(folder_content, extension + "\\" + folder_content)
            except FileNotFoundError:
                print("Unable to locate file")









main()


