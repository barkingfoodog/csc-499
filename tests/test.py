import unittest
import filecmp
import os
import sys
# put our src dir in the system path so we can import main and sort
dir_path = os.getcwd()
dir_path = dir_path[0 : dir_path.rfind('/')] + '/src'
sys.path.append(dir_path)
import main
import sort

class Tests(unittest.TestCase):

    # test the output of main against our expected output
    def test_output(self):
        # path to input data
        input_path = os.getcwd() + '/data/input.txt'
        # path where output will be located
        output_path = os.getcwd() + '/data/output.txt'
        # expected output, file to test output against
        expected_output_path = os.getcwd() + '/data/expected_output.txt'
        
        # list of arguments to pass to main
        args = list()
        # add the input path
        args.append(input_path)
        # add the output path
        args.append(output_path)
        # call main
        main.main(args) # outputs to output_path
        
        # compare the two files and return True if they are identical, False otherwise
        same_output = filecmp.cmp(output_path, expected_output_path)
        self.assertTrue(same_output) 

    # testing the partition_by_length method in sort.py
    def test_sort_partition(self):
        input_list = ['a', 'bb', 'aaa', 'c', 'aa', 'cccc', 'bbb']
        # the method should partition the input list into this output list
        output_list = [['a', 'c'], ['bb', 'aa'], ['aaa', 'bbb'], ['cccc']]
        self.assertEqual(sort.partition_by_len(input_list), output_list)

        input_list = ['aaa', 'aa', 'a']
        output_list = [['a'], ['aa'], ['aaa']]
        self.assertEqual(sort.partition_by_len(input_list), output_list)

    # testing the final sort method in sort.py
    # this method calls the partition_by_len method on the list
    # and then sorts the output alphabetically
    def test_final_sort(self):
        input_list = ['a', 'bb', 'aaa', 'c', 'aa', 'cccc', 'bbb']
        # the input should be sorted by len then alphabetically
        output_list = ['a', 'c', 'aa', 'bb', 'aaa', 'bbb', 'cccc']
        self.assertEqual(sort.sort(input_list), output_list)

        input_list = ['aaa', 'aa', 'a']
        output_list = ['a', 'aa', 'aaa']
        self.assertEqual(sort.sort(input_list), output_list)
if __name__ == '__main__':
    unittest.main()
