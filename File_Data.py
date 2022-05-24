#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:35:40 2022

@author: Sydney
"""
from Person import Person

class FileData:
    
    def __init__(self, filePath):
        rawFileData = []  
        try:
            with open(filePath) as f:
                rawFileData = f.readlines()
        except FileNotFoundError:
            print("\nError, file was not found. Please check input file path.\n")
            raise FileNotFoundError
        else:
            f.close()
        if len(rawFileData) < 1:
            raise Exception("Error: file must not be empty.")
        self.rawFileData = rawFileData
    
    def __get_deliminator(self, firstLine):
        if "," in firstLine:
            return ", "
        elif "|" in firstLine:
            return " | "
        else:
            return " "
    
    def parse_file_to_person_list(self):
        personList = []
        firstLine = self.rawFileData[0]
        deliminator = self.__get_deliminator(firstLine)

        for line in self.rawFileData:
            personData = line.strip().split(deliminator)

            if deliminator == " | " or deliminator == " ":
                if len(personData) != 6:
                    raise Exception("Line in file must contain 6 arguments. ", line)
            else:
                if len(personData) != 5:
                    raise Exception("Line in file must contain 5 arguments. ", line)

            lastName = personData[0]
            firstName = personData[1]
            gender = "" 
            favoriteColor = ""
            dateOfBirth = ""

            if deliminator == " | ":
                gender = personData[3]
                favoriteColor = personData[4]
                dateOfBirth = personData[5]
            elif deliminator == " ":
                gender = personData[3]
                favoriteColor = personData[5]
                dateOfBirth = personData[4]
            else:
                gender = personData[2]
                favoriteColor = personData[3]
                dateOfBirth = personData[4]
                    
            person = Person(lastName, firstName, gender, dateOfBirth, favoriteColor)
            personList.append(person)
        return personList