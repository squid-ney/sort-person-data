#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 13:24:53 2022

@author: Sydney
"""

import unittest
import Person


class TestPerson(unittest.TestCase):
    
    def test_create_person(self):
        """
        Test Person object is created
        """
        lastName = "testLastName"
        firstName = "testFirstName"
        gender = "Female"
        dateOfBirth = "5/22/2022"
        favoriteColor = "Yellow"
        person = Person.Person(lastName, firstName, gender, dateOfBirth, favoriteColor)
        
        self.assertEqual(person.lastName, lastName)
        self.assertEqual(person.firstName, firstName)
        self.assertEqual(person.gender, gender)
        self.assertEqual(person.dateOfBirth, dateOfBirth)
        self.assertEqual(person.favoriteColor, favoriteColor)

    def test_creat_person_format_birth_date(self):
        """
        Test date of birth is formatted when Person object is created
        """
        expectedDateOfBirth = "5/22/2022"
        lastName = "testLastName"
        firstName = "testFirstName"
        gender = "Female"
        dateOfBirth = "5-22-2022"
        favoriteColor = "Yellow"
        person = Person.Person(lastName, firstName, gender, dateOfBirth, favoriteColor)
        
        self.assertEqual(person.dateOfBirth, expectedDateOfBirth)
        
    def test_creat_person_format_gender_f(self):
        """
        Test gender is formatted when Person object is created (Female)
        """
        expectedGender = "Female"
        lastName = "testLastName"
        firstName = "testFirstName"
        gender = "F"
        dateOfBirth = "5-22-2022"
        favoriteColor = "Yellow"
        person = Person.Person(lastName, firstName, gender, dateOfBirth, favoriteColor)
        
        self.assertEqual(person.gender, expectedGender)
        
    def test_creat_person_format_gender_m(self):
        """
        Test gender is formatted when Person object is created (Male)
        """
        expectedGender = "Male"
        lastName = "testLastName"
        firstName = "testFirstName"
        gender = "M"
        dateOfBirth = "5-22-2022"
        favoriteColor = "Yellow"
        person = Person.Person(lastName, firstName, gender, dateOfBirth, favoriteColor)
        
        self.assertEqual(person.gender, expectedGender)
        
if __name__ == '__main__':
    unittest.main()