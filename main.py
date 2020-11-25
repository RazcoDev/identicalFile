from os import listdir, stat
from os.path import isfile, join


def same_file_detector(path):
    # reading the files and add them to a list as a dict : {'name': 'x','size':123}.
    files_list = [{'name': path +'/'+ file, 'size': stat(path +'/'+ file).st_size} for file in listdir(path) if
                  isfile(join(path, file))]
    # sorting the list.
    files_list.sort(key=lambda file: stat(file['name']).st_size, reverse=True)

    files_size_dict = {}
    hash_file_dict = {}

    # append the files to a list by their size, the size is a key on the dict.
    for file in files_list:
        if file['size'] not in files_size_dict.keys():
            files_size_dict[file['size']] = []
        files_size_dict[file['size']].append(file)

    # append the files to a list by their hashed content, the hashed content is a key on the dict.
    for size in files_size_dict.keys():
        for file in files_size_dict[size]:
            file_content = open(file['name'], 'r').read()
            hashed_content = str(hash(file_content))
            if hashed_content not in hash_file_dict.keys():
                hash_file_dict[hashed_content] = []
            hash_file_dict[hashed_content].append(file)

    # prints the files that are having the same hased value.
    for hash_key in hash_file_dict.keys():
        print(f"Those files are the same : {hash_file_dict[hash_key]} ")

if __name__ == '__main__':
    path = '/Users/razco/Raz/test'
    same_file_detector(path)