with open("info_regarding_previous_use.txt", 'r')as previous_use:
    if previous_use.read() == 's':
        print("S is Present")
    else:
        print("S is Abesent")
