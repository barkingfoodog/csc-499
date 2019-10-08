import sys
# returns the file read from the file_path, if valid
def read_file(file_path):

    # attempt to read the file_path into a file
    try:
        # open our file and store it into name list
        with open(file_path) as name_list:
            # new list for the parsed names
            parsed_names = list()

            # for each name in the list, strip whitespaces
            for name in name_list:
                # if name has at least one character, add it
                if len(name.strip()) > 0:
                    parsed_names.append(name.strip())
            return parsed_names

    # could not read the file successfully
    except Exception as e:
        # print the error
        print(e)
        
        # quit the program
        sys.exit(0)
