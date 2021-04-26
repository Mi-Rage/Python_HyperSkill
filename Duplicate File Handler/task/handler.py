import sys
import os


def get_file_format():
    print("Enter file format:")
    return input()


def get_sort_option():
    print("Size sorting options:")
    print("1. Descending")
    print("2. Ascending")
    while True:
        option = int(input())
        if option == 1:
            return True
        elif option == 2:
            return False
        else:
            print("Wrong option")
            print("Size sorting options:")


def sorted_output(dictionary, sort):
    sorted_keys = sorted(dictionary.keys(), reverse=sort)
    for key in sorted_keys:
        print(key, " bytes")
        values = dictionary.get(key)
        for v in values:
            print(v)


def check_args():
    args = sys.argv
    if len(args) == 1:
        print("Directory is not specified")
        sys.exit(0)
    return args[1]


req_dir = check_args()
file_format = '.' + get_file_format()
sort_option = get_sort_option()

storage = {}
for root, dirs, files in os.walk(req_dir):
    for name in files:
        if file_format in name:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            if size in storage.keys():
                list_files = storage.get(size)
                list_files.append(path)
                storage.update({size: list_files})
            else:
                storage.update({size: [path]})

sorted_output(storage, sort_option)
