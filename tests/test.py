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
        # testing with the asc flag

        # path to input data
        input_path = os.getcwd() + '/data/input.txt'
        # path where output will be located
        output_path = os.getcwd() + '/data/output.txt'
        # expected output, file to test output against
        expected_output_path_asc = os.getcwd() + '/data/expected_output_asc.txt'
        
        # list of arguments to pass to main
        args = list()
        # add the input path
        args.append(input_path)
        # add the output path
        args.append(output_path)
        # add the ascending argument
        args.append('asc')
        # call main
        main.main(args) # outputs to output_path
        
        # compare the two files and return True if they are identical, False otherwise
        same_output = filecmp.cmp(output_path, expected_output_path_asc)
        self.assertTrue(same_output) 

        # testing with the desc flag

        expected_output_path_desc = os.getcwd() + '/data/expected_output_desc.txt'

        # list of arguments to pass to main
        args = list()
        # add the input path
        args.append(input_path)
        # add the output path
        args.append(output_path)
        # add the ascending argument
        args.append('desc')
        # call main
        main.main(args) # outputs to output_path
        
        # compare the two files and return True if they are identical, False otherwise
        same_output = filecmp.cmp(output_path, expected_output_path_desc)
        self.assertTrue(same_output) 

    '''
        testing the partition_by_length method in sort.py
    '''
    def test_sort_partition(self):
        '''
            testing partition with asc flag

            the method should partition the input list into this output list
            which is in ascending order by length
        '''
        input_list = ['a', 'bb', 'aaa', 'c', 'aa', 'cccc', 'bbb']
        output_list = [['a', 'c'], ['bb', 'aa'], ['aaa', 'bbb'], ['cccc']]
        self.assertEqual(sort.partition_by_len(input_list, 'asc'), output_list)

        input_list = ['aaa', 'aa', 'a']
        output_list = [['a'], ['aa'], ['aaa']]
        self.assertEqual(sort.partition_by_len(input_list, 'asc'), output_list)

        '''
            testing partition with the desc flag 

            the method should partition the input list into this output list
            which is in descending order by length
        '''
        input_list = ['a', 'bb', 'aaa', 'c', 'aa', 'cccc', 'bbb']
        output_list = [['cccc'], ['aaa', 'bbb'], ['bb', 'aa'], ['a', 'c']]
        self.assertEqual(sort.partition_by_len(input_list, 'desc'), output_list)

        input_list = ['a', 'aa', 'aaa']
        output_list = [['aaa'], ['aa'], ['a']]
        self.assertEqual(sort.partition_by_len(input_list, 'desc'), output_list)


    '''
        testing the sort_by_alpha method
    '''
    def test_sort(self):
        input_dict = [['c', 'a'], ['bb', 'aa'], ['bbb', 'aaa'], ['cccc']]
        output_list = [['a', 'c'], ['aa', 'bb'], ['aaa', 'bbb'], ['cccc']]
        self.assertEqual(sort.sort_by_alpha(input_dict), output_list)

        input_list = [['aaa'], ['aa'], ['a']]
        output_list = [['aaa'], ['aa'], ['a']]
        self.assertEqual(sort.sort_by_alpha(input_list), output_list)

    '''
        testing the sort_by_len_alpha method in sort.py

        this method calls the partition_by_len method on the list
        and then sorts the output alphabetically
    '''
    def test_sort_by_len_alpha(self):
        '''
            testing the sorting method that sorts by length and alphabetically
            with the asc flag

            this method should sort the input list into the output list
            which is in ascending order 
        '''
        input_list = ['a', 'bb', 'aaa', 'c', 'aa', 'cccc', 'bbb']
        output_list = ['a', 'c', 'aa', 'bb', 'aaa', 'bbb', 'cccc']
        self.assertEqual(sort.sort_by_len_alpha(input_list, 'asc'), output_list)

        input_list = ['aaa', 'aa', 'a']
        output_list = ['a', 'aa', 'aaa']
        self.assertEqual(sort.sort_by_len_alpha(input_list, 'asc'), output_list)


        '''
            testing the sorting method that sorts by length and alphabetically
            with the desc flag

            this method should sort the input list into the output list
            which is in descending order 
        '''
        input_list = ['a', 'bb', 'aaa', 'c', 'aa', 'cccc', 'bbb']
        output_list = ['cccc', 'aaa', 'bbb', 'aa', 'bb', 'a', 'c']
        self.assertEqual(sort.sort_by_len_alpha(input_list, 'desc'), output_list)

        input_list = ['a', 'aa', 'aaa']
        output_list = ['aaa', 'aa', 'a']
        self.assertEqual(sort.sort_by_len_alpha(input_list, 'desc'), output_list)

if __name__ == '__main__':
    unittest.main()
