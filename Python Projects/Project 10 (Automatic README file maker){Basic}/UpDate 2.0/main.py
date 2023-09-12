# Date 13-09-2021

from all_function_file_for_main import *


location = get_path()

extension = input(
    "Please enter the Extension of your file, for example - py, cpp, html, js etc.\n")

list_of_files = list_all_files_of_directory(location, extension=extension)
appending_all_files_to_txt_file(location, list_of_files)


print(
    f"\nThe list of your files are as follows:")
for file in list_of_files:
    print(f"{file}")
print(
    f"And they are also in file named \"list_of_files.txt\", which is created in the below given directory\n{location}")

print(
    f"To get README MarkDown file follow the following Steps:\nStep 1: Go to the file named \"list_of_files.txt\" which is located in the same path as of the path feeded.\nStep 2: Arrange those files in order you need.\nStep 3: Save file \"list_of_files.txt\".\nStep 4: Come again to the program window and enter C to generate file.\n\nNote: If you get confused from the above \'Steps\' you can see attached video in zip file.\n\n\n")


try:
    choice = input("Enter C if you arranged files in order\n").lower()
except:
    print("Please wait while we are generating your README")
    choice = 'c'

if choice == 'c':
    with open(f"{location}/list_of_files.txt", 'r') as file:
        list_of_files = file.read()
    list_of_files = list_of_files.split('\n')[:-1]

    readme_constructor(file_name="README", main_title="TEST", code_file_names_list=list_of_files,
                       which_type_of_code_file_it_is="C++", which_type_of_code_file_name_to_print_in_README="C/C++", code_Serial_number=True)
