# Date 27-06-2021
from os import listdir
from os.path import isfile, join

mypath = input("Enter the path of your directory\n")
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# onlyfiles.sort()
for i in onlyfiles:
    print(i)
