#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:35:40 2022

@author: Sydney
"""
from Person import Person
from datetime import datetime

class FileData:

    def __init__(self, filePath):
        self.elementList = []
        rawFileData = []
        
        try:
            with open(filePath) as f:
                rawFileData = f.readlines()
        except FileNotFoundError:
            print("\nError, file was not found. Please check input file path.\n")
            raise
        else:
            f.close()

        firstLine = rawFileData[0]
        deliminator = self.__get_deliminator(firstLine)
                
        for line in rawFileData:
            personData = line.strip().split(deliminator)
    
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
            self.elementList.append(person) 

    def __get_deliminator(self, firstLine):
        if "," in firstLine:
            return ", "
        elif "|" in firstLine:
            return " | "
        else:
            return " "
        
    def __sort_key_last_name(self, person):
            return person.lastName
    
    def __sort_people(self, people, sort_key, reverse=False):
        return sorted(people, key=sort_key, reverse=reverse)
    
    def sort_by_gender_then_lastname(self):
        females = []
        males = []

        for person in self.elementList:
            if person.gender == "Female":
                females.append(person)
            if person.gender == "Male":
                males.append(person)  
        
        femalesByLastName = self.__sort_people(females, self.__sort_key_last_name)
        malesByLastName = self.__sort_people(males, self.__sort_key_last_name)
        sortedByGenderAndLastName = femalesByLastName + malesByLastName
        return sortedByGenderAndLastName

    def sort_by_birth_then_lastname(self):
        def sort_key_birth_date_then_last_name(person):
            return datetime.strptime(person.dateOfBirth, '%m/%d/%Y'), person.lastName
        
        return self.__sort_people(self.elementList, sort_key_birth_date_then_last_name)

    def sort_by_last_name_desc(self):
        reverse = True
        return self.__sort_people(self.elementList, self.__sort_key_last_name, reverse) 
    
    def print_element_list(self, providedList=None):
        listToPrint = []
        if providedList:
            listToPrint = providedList
        else:
            listToPrint = self.elementList
            
        for element in listToPrint:
            element.printPerson()