import os

# CONFIG:

file_exts = ["csv"]

# CONFIG END

def CheckFile(filename): # Requires a path to file

    if os.path.exists(filename):
        print(f"INFO: File {filename} was found.")

    else:
        print(f"ERROR: File {filename} could not be found.")
        raise ValueError

def CheckFileExt(filename): # Requires a path to file

    ext = filename.split(".")[-1]

    if ext not in file_exts:
        print(f"ERROR: Extension {ext} not supported.")
        print(f"Currently supported extension are: {file_exts}")
        raise ValueError

def GetValidFile():

    name = input("Please enter a file path: ")

    while True:

        try:
            CheckFile(name)
            CheckFileExt(name)
        
        except ValueError:
            name = input("Please try again: ")

        except Exception as ex:
            print(f"ERROR: Unknown error occurred: {ex}")
            break

        else:
            break
    
    return name