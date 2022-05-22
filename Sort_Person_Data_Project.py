#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:52:13 2022

@author: Sydney
"""
import FileData


def main():
   filePath = 'def-method-code-test-input-files/comma.txt'
   fileData = FileData.FileData(filePath)

   sortedByGenderThenLastName = fileData.sort_by_gender_then_lastname()
   sortedByBirthDateThenLastName = fileData.sort_by_birth_then_lastname()
   sortedByLastNameDesc = fileData.sort_by_last_name_desc()
   
   print("Output 1:")
   fileData.print_element_list(sortedByGenderThenLastName)
   print("\nOutput 2:")
   fileData.print_element_list(sortedByBirthDateThenLastName)
   print("\nOutput 3:")
   fileData.print_element_list(sortedByLastNameDesc)
  
                 
main()
    
    
    