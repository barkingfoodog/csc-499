import read
import os
def main():
    file_path = os.getcwd()
    file_path = file_path[0 : file_path.rfind('/')] + '/ExamResources/Sort Me.txt'
    read.read_file(file_path)

    pass





if __name__ == '__main__':
    main()