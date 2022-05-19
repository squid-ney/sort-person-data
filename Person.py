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
        self.gender = gender
        self.dateOfBirth = dateOfBirth
        self.favoriteColor = favoriteColor
 
    def printPerson(self):
        print(self.lastName, self.firstName, self.gender, self.dateOfBirth, self.favoriteColor)

