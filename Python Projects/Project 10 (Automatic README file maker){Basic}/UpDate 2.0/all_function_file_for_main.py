# Date 13-09-2021

from mdutils.mdutils import MdUtils
import os
import glob
from pyperclip import paste as pa
from pyperclip import copy as co


def readme_constructor(file_name="README", main_title="This is a Main Title", code_file_names_list=["check_1.py"], which_type_of_code_file_it_is="python", which_type_of_code_file_name_to_print_in_README="Python", code_Serial_number=False):

    main_title = f"<h1 style=\"text-align:center; font-size:360%; font-family:verdana;color:#4A3E76;\"><em>{main_title}</em></h1>"
    mdFile = MdUtils(file_name=file_name, title=main_title, author="Aman")

    mdFile.write('# These tutorials are watched from [**_CodeWithHarry_**](https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww "Clike here to checkout his channel") YouTube channel from [**_Pyton Playlist_**](https://youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME "Clike here to check out his Python tutorials Playlist")\n')

    mdFile.write(5*'---\n')

    i = 0
    while i < len(code_file_names_list):
        try:
            file_code = open(f"{code_file_names_list[i]}", 'r').read()
            # mdFile.write("<br>")
            if code_Serial_number == False:
                mdFile.write(
                    f"## **_{str(code_file_names_list[i]).split('.')[0]} of {which_type_of_code_file_name_to_print_in_README}_**\n")
            else:
                mdFile.write(
                    f"## **_{i+1}.) {str(code_file_names_list[i]).split('.')[0]} of {which_type_of_code_file_name_to_print_in_README}_**\n")
            mdFile.write(
                f"### [**_Click me_**]({code_file_names_list[i]} \"Clike here to see full file\") to see full file of {str(code_file_names_list[i]).split('.')[0]}\n")

            mdFile.write(
                f"```{which_type_of_code_file_it_is}\n{str(file_code)}\n```\n")
            mdFile.write(2*'---\n')
        except Exception as e:
            print(
                f"There is no such file named \"{code_file_names_list[i]}\" or the problem is the following\n{e}")
        i += 1

    mdFile.create_md_file()


def get_path():
    try:
        mypath = pa()
        # print(mypath)
        with open(mypath+"\check.txt", 'w'):
            # print("check 1 Done(creating check file)")
            pass
        os.remove(mypath+"\check.txt")
        # print("check 2 Done(deleting check file)")
        # print("check 3 Sucessfull(path is valid)\n\n")
    except:
        mypath = input("Please Enter the directory of your folder\n")

    return mypath


def list_all_files_of_directory(location, extension="py"):
    list_of_files = []
    os.chdir(location)
    for file in glob.glob(f"*.{extension}"):
        list_of_files.append(file)
    return list_of_files


def appending_all_files_to_txt_file(location, list_of_files):
    with open(f"{location}/list_of_files.txt", 'w')as list_of_file:
        for file in list_of_files:
            list_of_file.write(f"{file}\n")


if __name__ == '__main__':
    # readme_constructor(code_file_names_list=['all_function_file_for_main.py', 'check_1.py', 'check_10.py', 'check_11.py', 'check_12.py', 'check_13.py', 'check_14.py', 'check_15.py', 'check_16.py', 'check_17.py',
    #                    'check_18.py', 'check_19.py', 'check_2.py', 'check_20.py', 'check_3.py', 'check_4.py', 'check_5.py', 'check_6.py', 'check_7.py', 'check_8.py', 'check_9.py', 'main.py'])

    location = get_path()
    li = list_all_files_of_directory(location, extension="cpp")
    appending_all_files_to_txt_file(location, li)

    readme_constructor(file_name="README", main_title="This is a Main Title",
                       code_file_names_list=li, which_type_of_code_file_it_is="C++")
