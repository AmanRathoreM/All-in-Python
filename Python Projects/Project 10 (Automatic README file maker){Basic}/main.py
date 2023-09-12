# Date 27-06-2021

# * C:\Google Drive\Programming\Python\Python tp Projects\Project 10 (Automatic README file maker){Basic}\tp
from all_function_file_for_main import readme_constructor as rc
from glob import glob
from os import listdir
from os.path import isfile, join
import os
from pyperclip import paste as pa
from pyperclip import copy as co
from time import time

try:
    mypath = pa()
    with open(mypath+"\check.txt", 'w'):
        print("check 1 Done(creating check file)")
        pass
    os.remove(mypath+"\check.txt")
    print("check 2 Done(deleting check file)")
    print("check 3 Sucessfull(path is valid)\n\n")
except:
    mypath = input("Please Enter the directory of your folder\n")


extension = input('Please enter the extension of your code files\n')

os.chdir(mypath)
files = []
for file in glob(f"*.{extension}"):
    files.append(file)


print(
    f"\nThe list of your files are as follows")
for i in files:
    print(i)
print(f"And they are also in file named list_of_files\n")

print(
    f"To get README MarkDown file follow the following Steps\nStep 1: Go to the file named list_of_files.txt which is located in the same path as of this the path you entered.\nStep 2: Arrange those files in order you need.\nStep 3: Save that file(list_of_files.txt).\nStep 4: Come again to the program window and enter c to generate file.\n\nNote 1: If there is any missing file in that list then please add that name; We will try to fix this bug in next UpDate.\nNote 2: The file of MarkDown will be in raw form and it will also not be formated.\nNote 3: If you get confused from the above \'Steps\' or \'Note\' you can see attached video explanation\n\n\n")

with open("list_of_files.txt", 'w') as file1:
    file1.write(str(files[0])+'\n')
    i = 1
    with open("list_of_files.txt", 'a') as file1_1:
        while i < len(files):
            file1_1.write(str(files[i])+'\n')
            i += 1


try:
    choice = input("Enter C if you arranged files in order\n").lower()
except:
    print("Please wait whle we are generating your files")
    choice = 'c'

files = open('list_of_files.txt', 'r').readlines()

file_names = []
for string in files:
    sorted_string = string.replace('\n', '')
    file_names.append(sorted_string)

time_when_started = float(time())
rc(main_title="Automatic MarkDown README Generator",
   code_file_names_list=file_names, which_type_of_code_file_it_is="c")
print(
    f"Your README is generated in {float(time())-float(time_when_started)} Seconds")
