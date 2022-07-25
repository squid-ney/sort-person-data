#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:35:40 2022

@author: Sydney
"""
from datetime import datetime

class SortPeople:

    def __init__(self, personList):
        self.personList = personList
         
    def __sort_key_last_name(self, person):
            return person.lastName
    
    def __sort_people(self, people, sort_key, reverse=False):
        return sorted(people, key=sort_key, reverse=reverse)
    
    def sort_by_gender_then_lastname(self):
        females = []
        males = []

        for person in self.personList:
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
        
        return self.__sort_people(self.personList, sort_key_birth_date_then_last_name)

    def sort_by_last_name_desc(self):
        reverse = True
        return self.__sort_people(self.personList, self.__sort_key_last_name, reverse) 
    
    def print_element_list(self, providedList=None):
        listToPrint = []
        if providedList:
            listToPrint = providedList
        else:
            listToPrint = self.personList
            
        for element in listToPrint:
            element.printPerson()