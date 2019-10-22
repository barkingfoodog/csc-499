#!/usr/bin/python3

'''
Author: Trevor Rice
Class: CSC 499
Assignment: Homework1
Github: https://github.com/TrevorRice39/csc-499/blob/master/Homework1
'''
import sys, getopt
import read
import sort as sort_names

def main(argv):
    new_path = argv[0]
    # reading the file and parsing the names
    name_list = read.read_file(new_path)
    print(new_path)
    # print the sorted list
    print('Sorted file:\n', sort_names.sort(name_list))

if __name__ == '__main__':
    main(sys.argv[1:])