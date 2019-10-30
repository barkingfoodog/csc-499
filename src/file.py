import sys

# returns the file read from the file_path, if valid
def read(file_path):
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
                    # strip the whitespaces and append it to our list
                    parsed_names.append(name.strip())
            return parsed_names

    # could not read the file successfully
    except Exception as e:
        # print the error
        print(e)
        
        # quit the program
        sys.exit(0)

# writes 'data' to the file_path file
def write(file_path, data):
    try:
        # writing the list of sorted names to the output file
        with open(file_path, 'w') as output_file:
            for line in data:
                output_file.write('%s\n' % line)
    except Exception as e:
        # print the error
        print(e)
        
        # quit the program
        sys.exit(0)
