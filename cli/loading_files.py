import os
import questionary
import pandas as pd

def clear():
    """
    Clears Python console
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Mac and Linux
    else:
        _ = os.system('clear')

# Load data
def select_file_type():
    """

    """
    return questionary.select(
        "What type of file do you want to load?",
        choices=[
            "CSV",
            "Excel",
            "HTML"
        ]).ask()


def browse_file_search():
    """

    """
    file_path = os.getcwd()

    while(not os.path.isfile(file_path)):
        # Display the existing folders/files and let the user choose
        list_files_directory = [".."]
        for file in os.listdir(file_path):
            if(os.path.isdir(os.path.join(file_path, file))):
                file = "[D -> " + file + "]"
            else:
                file = "[F -> " + file + "]"
            list_files_directory.append(file)
        
        # Order the list
        list_files_directory.sort()

        add_to_path = questionary.select(
            "Select your file",
            choices=list_files_directory
        ).ask()

        if(add_to_path != ".."):
            file_path = os.path.join(file_path, add_to_path[6:-1])
        else: 
            file_path = os.path.join(file_path, "..")
        clear()
    
    return file_path

def read_file(filetype, filepath, sheetname=None):
    """

    """
    if(filetype == "CSV"):
        df = pd.read_csv(filepath)
    elif(filetype == "Excel"):
        df = pd.read_excel(filepath, sheetname=sheetname)
    elif(filetype == "HTML"):
        df = pd.read_html(filepath)

    try: 
        return df
    except: 
        print("ERROR: This file type hasn't been implemented yet")