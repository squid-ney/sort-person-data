#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 17:58:54 2022

@author: Sydney
"""

class Person:
    def __init__(self, lastName, firstName, gender, dateOfBirth, favoriteColor):
        self.lastName = lastName
        self.firstName = firstName
        self.gender = self.format_gender(gender)
        self.dateOfBirth = self.format_birth_date(dateOfBirth)
        self.favoriteColor = favoriteColor
 
    def format_birth_date(self, birthDate):
        return birthDate.replace('-','/')

    def format_gender(self, gender):
        if gender == 'F':
            return "Female"
        elif gender == 'M':
            return "Male" 
        else:
            return gender
    
    def printPerson(self):
        print(self.lastName, self.firstName, self.gender, self.dateOfBirth, self.favoriteColor)

