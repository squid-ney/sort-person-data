#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:52:13 2022

@author: Sydney
"""
from File_Data import FileData
from Sort_People import SortPeople
import sys

def main(): 
    args = sys.argv
    if len(args) < 2:
        raise "Error, no file path argument provided."
    
    filePath = args[1]
    fileDataObject = FileData(filePath)
    
    personList = fileDataObject.parse_file_to_person_list()
    sortPeopleObject = SortPeople(personList)

    sortedByGenderThenLastName = sortPeopleObject.sort_by_gender_then_lastname()
    sortedByBirthDateThenLastName = sortPeopleObject.sort_by_birth_then_lastname()
    sortedByLastNameDesc = sortPeopleObject.sort_by_last_name_desc()
   
    print("Output 1:")
    sortPeopleObject.print_element_list(sortedByGenderThenLastName)
    print("\nOutput 2:")
    sortPeopleObject.print_element_list(sortedByBirthDateThenLastName)
    print("\nOutput 3:")
    sortPeopleObject.print_element_list(sortedByLastNameDesc)

if __name__ == "__main__":
    main()               
    
    
    