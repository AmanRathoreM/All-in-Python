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
