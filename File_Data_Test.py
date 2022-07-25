#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:23:55 2022

@author: Sydney
"""

import unittest
from unittest.mock import patch, mock_open
from File_Data import FileData
from Person import Person

class TestFileData(unittest.TestCase):
    mockEmptyFileData = ""
    mockPipeFileData = "Smith | Steve | D | M | Red | 3-3-1985\nBonk | Radek | S | M | Green | 6-3-1975"
    mockSpaceFileData = "Kournikova Anna F F 6-3-1975 Red\nHingis Martina M F 4-2-1979 Green"
    mockCommaFileData = "Bishop, Timothy, Male, Yellow, 4/23/1967\nAbercrombie, Neil, Male, Tan, 2/13/1943\nKelly, Sue, Female, Pink, 7/12/1959\nGerard, Neil, Male, Tan, 2/13/1943"   
    
    @patch('builtins.open', mock_open(read_data='mock 123\ntest :)'))
    def test_initialize_file_data_object_success(self):
            """
            Test succesfully initializing file data from a given file path
            """
            fileName = '/mockFile'
            expectedParsedFileData = ['mock 123\n','test :)']
            
            fileData = FileData(fileName)
            actualParsedFileData = fileData.rawFileData
            
            self.assertEqual(expectedParsedFileData, actualParsedFileData)
            
    @patch('builtins.open', new_callable=mock_open)
    def test_initialize_file_data_object_error(self, m):
            """
            Test exception is raised when file path is not provided
            """
            fileName = '/mockFile'
            m.side_effect = FileNotFoundError()
            
            with self.assertRaises(FileNotFoundError):
                FileData(fileName)
                
    @patch('builtins.open', mock_open(read_data=mockEmptyFileData))
    def test_initialize_file_data_object_empty_file(self):
            """
            Test exception is raised when file is empty
            """
            fileName = '/mockFile'
            with self.assertRaises(Exception):
                FileData(fileName)  
                        
    @patch('builtins.open', mock_open(read_data=mockCommaFileData))
    def test_parse_file_to_person_list_comma_deliminator(self):
            """
            Test parsing file with comma deliminator
            """
            fileName = '/mockFile'
            
            person1 = Person("Bishop", "Timothy", "Male", "4/23/1967", "Yellow")
            person2 = Person("Abercrombie","Neil", "Male","2/13/1943","Tan")
            person3 = Person("Kelly","Sue", "Female","7/12/1959","Pink")
            person4 = Person("Gerard","Neil", "Male","2/13/1943","Tan")
            
            expectedPersonList = [person1, person2, person3, person4]
            fileData = FileData(fileName)
            actualPersonList= fileData.parse_file_to_person_list()
            
            self.assertEqual(expectedPersonList[0].lastName, actualPersonList[0].lastName)
            self.assertEqual(expectedPersonList[0].gender, actualPersonList[0].gender)
            self.assertEqual(expectedPersonList[2].lastName, actualPersonList[2].lastName)
            self.assertEqual(expectedPersonList[2].gender, actualPersonList[2].gender)
            
    @patch('builtins.open', mock_open(read_data=mockSpaceFileData))
    def test_parse_file_to_person_list_space_deliminator(self):
            """
            Test parsing file with space deliminator
            """
            fileName = '/mockFile'
            
            person1 = Person("Kournikova", "Anna", "F", "6-3-1975", "Red")
            person2 = Person("Hingis","Martina", "F","4-2-1979","Green")

            expectedPersonList = [person1, person2]
            fileData = FileData(fileName)
            actualPersonList= fileData.parse_file_to_person_list()
            
            self.assertEqual(expectedPersonList[0].lastName, actualPersonList[0].lastName)
            self.assertEqual(expectedPersonList[0].gender, actualPersonList[0].gender)
            self.assertEqual(expectedPersonList[1].lastName, actualPersonList[1].lastName)
            self.assertEqual(expectedPersonList[1].gender, actualPersonList[1].gender)
    
    @patch('builtins.open', mock_open(read_data=mockPipeFileData))
    def test_parse_file_to_person_list_pipe_deliminator(self):
            """
            Test parsing file with pipe deliminator
            """
            fileName = '/mockFile'
            
            person1 = Person("Smith", "Steve", "M", "3-3-1985", "Red")
            person2 = Person("Bonk","Radek", "M","6-3-1975","Green")

            expectedPersonList = [person1, person2]
            fileData = FileData(fileName)
            actualPersonList= fileData.parse_file_to_person_list()
            
            self.assertEqual(expectedPersonList[0].lastName, actualPersonList[0].lastName)
            self.assertEqual(expectedPersonList[0].gender, actualPersonList[0].gender)
            self.assertEqual(expectedPersonList[1].lastName, actualPersonList[1].lastName)
            self.assertEqual(expectedPersonList[1].gender, actualPersonList[1].gender)
            
            
if __name__ == '__main__':
    unittest.main()

