import sys
import os
import hashlib


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


def check_args():
    args = sys.argv
    if len(args) == 1:
        print("Directory is not specified")
        sys.exit(0)
    return args[1]


def get_check_duplicates():
    print("Check for duplicates?")
    while True:
        answer = input()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print("Wrong option")
            print("Check for duplicates?")


def get_double_sized():
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
    # Тут удалим все эелемены где менее двух совпадений
    to_del = []
    for s in storage.keys():
        if len(storage.get(s)) < 2:
            to_del.append(s)
    for s in to_del:
        del storage[s]

    return storage


def get_hashed_dict(dictionary):
    result = {}
    for file_size in dictionary.keys():
        hashes_dict = {}
        files_same_size = dictionary.get(file_size)
        for file in files_same_size:
            with open(file, mode='rb') as f:
                file_content = f.read()
            m = hashlib.md5()
            m.update(file_content)
            hash_file = m.hexdigest()
            if hashes_dict.get(hash_file, 'None') == 'None':
                hashes_dict.update({hash_file: [file]})
            else:
                file_paths = hashes_dict.get(hash_file)
                file_paths.append(file)
                hashes_dict.update({hash_file: file_paths})
        # Здесь удалим все вхождения хешей с к-вом путей меньше 2
        to_del = []
        for key in hashes_dict.keys():
            if len(hashes_dict.get(key)) < 2:
                to_del.append(key)
        for key in to_del:
            del hashes_dict[key]

        result.update({file_size: hashes_dict})
    return result


def sized_output(dictionary, sort):
    sorted_keys = sorted(dictionary.keys(), reverse=sort)
    for key in sorted_keys:
        print(key, " bytes")
        values = dictionary.get(key)
        for v in values:
            print(v)


def hashed_output(dictionary, sort):
    sorted_keys = sorted(dictionary.keys(), reverse=sort)
    count = 1
    for sizes in sorted_keys:
        print(sizes, 'bytes')
        for hash_file in dictionary.get(sizes).keys():
            print('Hash:', hash_file)
            for file_path in dictionary.get(sizes).get(hash_file):
                print(f"{count}. {file_path}")
                count += 1


req_dir = check_args()
file_format = '.' + get_file_format()
sort_option = get_sort_option()

double_sized_dict = get_double_sized()
sized_output(double_sized_dict, sort_option)

if get_check_duplicates():
    hashed_files_dict = get_hashed_dict(double_sized_dict)
    hashed_output(hashed_files_dict, sort_option)
