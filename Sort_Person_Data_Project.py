#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:52:13 2022

@author: Sydney
"""
from File_Data import FileData
import sys

def main(): 
    args = sys.argv
    if len(args) < 2:
        raise "Error, no file path argument provided."
    
    filePath = args[1]
    fileData = FileData(filePath)

    sortedByGenderThenLastName = fileData.sort_by_gender_then_lastname()
    sortedByBirthDateThenLastName = fileData.sort_by_birth_then_lastname()
    sortedByLastNameDesc = fileData.sort_by_last_name_desc()
   
    print("Output 1:")
    fileData.print_element_list(sortedByGenderThenLastName)
    print("\nOutput 2:")
    fileData.print_element_list(sortedByBirthDateThenLastName)
    print("\nOutput 3:")
    fileData.print_element_list(sortedByLastNameDesc)
    # def-method-code-test-input-files/comma.txt

if __name__ == "__main__":
    main()               
    
    
    