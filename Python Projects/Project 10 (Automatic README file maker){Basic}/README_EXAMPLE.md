
<h1 style="text-align:center; font-size:360%; font-family:verdana;color:#4A3E76;"><em>Automatic MarkDown README Generator</em></h1>

# These tutorials are watched from [**_Indian AI Production_**](https://www.youtube.com/channel/UCNzs7V6xG5GO0i_i6Grojyw "Clike here to checkout his channel") YouTube channel from [**_Seaborn Playlist_**](https://youtube.com/playlist?list=PLfP3JxW-T70HaBYwsSDadlS3v2VeALgYh "Clike here to check out his Seaborn tutorials Playlist")
---
---
---
---
---
## **_all_function_file_for_main.py_**
### [**_Click me_**](all_function_file_for_main.py "Clike here to see full file") to see full file of all_function_file_for_main.py
```python
# Date 27-06-2021

from mdutils.mdutils import MdUtils


def readme_constructor(file_name="README", main_title="This is a Main Title", code_file_names_list=["check_1.py"], which_type_of_code_file_it_is="python"):

    main_title = f"<h1 style=\"text-align:center; font-size:360%; font-family:verdana;color:#4A3E76;\"><em>{main_title}</em></h1>"
    mdFile = MdUtils(file_name=file_name, title=main_title, author="Aman")

    mdFile.write('# These tutorials are watched from [**_Indian AI Production_**](https://www.youtube.com/channel/UCNzs7V6xG5GO0i_i6Grojyw "Clike here to checkout his channel") YouTube channel from [**_Seaborn Playlist_**](https://youtube.com/playlist?list=PLfP3JxW-T70HaBYwsSDadlS3v2VeALgYh "Clike here to check out his Seaborn tutorials Playlist")\n')

    mdFile.write(5*'---\n')

    i = 0
    while i < len(code_file_names_list):
        try:
            file_code = open(f"{code_file_names_list[i]}", 'r').read()
            # mdFile.write("<br>")
            mdFile.write(f"## **_{code_file_names_list[i]}_**\n")
            mdFile.write(
                f"### [**_Click me_**]({code_file_names_list[i]} \"Clike here to see full file\") to see full file of {code_file_names_list[i]}\n")

            mdFile.write(
                f"```{which_type_of_code_file_it_is}\n{str(file_code)}\n```\n")
            mdFile.write(2*'---\n')
        except Exception as e:
            print(
                f"There is no such file named \"{code_file_names_list[i]}\" or the problem is the following\n{e}")
        i += 1

    mdFile.create_md_file()


if __name__ == '__main__':
    readme_constructor(code_file_names_list=['all_function_file_for_main.py', 'check_1.py', 'check_10.py', 'check_11.py', 'check_12.py', 'check_13.py', 'check_14.py', 'check_15.py', 'check_16.py', 'check_17.py',
                       'check_18.py', 'check_19.py', 'check_2.py', 'check_20.py', 'check_3.py', 'check_4.py', 'check_5.py', 'check_6.py', 'check_7.py', 'check_8.py', 'check_9.py', 'main.py'])

```
---
---
## **_main.py_**
### [**_Click me_**](main.py "Clike here to see full file") to see full file of main.py
```python
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
    f"To get README MarkDown file follow the following Steps\nStep 1: Go to the file named list_of_files.txt which is located in the same path as of this program.\nStep 2: Arrange those files in order you need.\nStep 3: Save that file(list_of_files.txt).\nStep 4: Come again to the program window and enter c to generate file.\n\nNote 1: If there is any missing file in that list then please add that name; We will try to fix this bug in next UpDate.\nNote 2: The file of MarkDown will be in raw form and it will also not be formated.\nNote 3: If you get confused from the above \'Steps\' or \'Note\' you can see attached video explanation\n\n\n")

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
   code_file_names_list=file_names, which_type_of_code_file_it_is="python")
print(
    f"Your README is generated in {float(time())-float(time_when_started)} Seconds")

```
---
---
## **_check_1.py_**
### [**_Click me_**](check_1.py "Clike here to see full file") to see full file of check_1.py
```python
# Date 27-06-2021
from os import listdir
from os.path import isfile, join

mypath = input("Enter the path of your directory\n")
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# onlyfiles.sort()
for i in onlyfiles:
    print(i)

```
---
---
## **_check_2.py_**
### [**_Click me_**](check_2.py "Clike here to see full file") to see full file of check_2.py
```python
import sorting

print(help(sorting.quick))

```
---
---
## **_check_3.py_**
### [**_Click me_**](check_3.py "Clike here to see full file") to see full file of check_3.py
```python
li1 = [10, 20, 2, 3, 4, 5]
li1.pop(1)
print(li1)

```
---
---
## **_check_4.py_**
### [**_Click me_**](check_4.py "Clike here to see full file") to see full file of check_4.py
```python
from glob import glob
from pyperclip import paste as pa
import os


mypath = pa()
os.chdir(mypath)
files = []
for file in glob("*.py"):
    files.append(file)


for i in files:
    print(i)

```
---
---
## **_check_5.py_**
### [**_Click me_**](check_5.py "Clike here to see full file") to see full file of check_5.py
```python
file = open('check_1.py', 'r').read()
print(file)

```
---
---
