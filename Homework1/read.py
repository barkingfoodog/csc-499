import os

def read_file(file_path):
    
    with open(file_path) as file:
        name_list = [line.strip() for line in file]
        print(name_list)