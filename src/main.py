#!/usr/bin/python3

'''
Author: Trevor Rice
Class: CSC 499
Assignment: Homework1
Github: https://github.com/TrevorRice39/csc-499/blob/master/Homework1
'''
import sys, getopt
import os
import file
import sort as sort_names

def main(argv):
    if len(argv) < 2:
        print('Please enter input and output files as arguments!')
        sys.exit(0)
    
    # first arg is input path
    input_path = argv[0]
    # second arg is output path
    output_path = argv[1]
    
    # reading the file and parsing the names
    name_list = file.read(input_path)

    # sorting the names
    sorted_name_list = sort_names.sort(name_list)

    # write the sorted names to the output file
    file.write(output_path, sorted_name_list)
    

if __name__ == '__main__':
    main(sys.argv[1:])