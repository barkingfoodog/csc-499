'''
Author: Trevor Rice
Class: CSC 499
Assignment: Homework1
Github: https://github.com/TrevorRice39/csc-499/blob/master/Homework1
'''
import read
import sort as sort_names

def main():
    # reading in the file path
    print('Enter a file to be sorted: ', end='')
    new_path = input()

    # reading the file and parsing the names
    name_list = read.read_file(new_path)

    # print the sorted list
    print('Sorted file:\n', sort_names.sort(name_list))

if __name__ == '__main__':
    main()