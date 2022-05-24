#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:28:19 2022

@author: Sydney
"""

import unittest
from Sort_People import SortPeople
from Person import Person


class TestSortPeople(unittest.TestCase):
    
    def test_sort_by_gender_then_lastname(self):
        """
        Test sorting the people list by gender then last name
        """
        person1 = Person("Bishop","Timothy", "Male","4/23/1967","Yellow")
        person2 = Person("Abercrombie","Neil", "Male","2/13/1943","Tan")
        person3 = Person("Gerard","Neil", "Male","2/13/1943","Tan")
        person4 = Person("Kelly","Sue", "Female","7/12/1959","Pink")
        peopleList = [person1, person2, person3, person4]
        
        sortPeople = SortPeople(peopleList)
        
        expectedSort = [person4, person2, person1, person3]
        actualSort = sortPeople.sort_by_gender_then_lastname()
        
        self.assertEqual(expectedSort, actualSort)
    
    def test_sort_by_birth_then_lastname(self):
        """
        Test sorting the people list by birth date then last name
        """
        person1 = Person("Bishop","Timothy", "Male","4/23/1967","Yellow")
        person2 = Person("Gerard","Neil", "Male","2/13/1943","Tan")
        person3 = Person("Abercrombie","Neil", "Male","2/13/1943","Tan")
        person4 = Person("Kelly","Sue", "Female","7/12/1959","Pink")
        peopleList = [person1, person2, person3, person4]
        
        sortPeople = SortPeople(peopleList)
        
        expectedSort = [person3, person2, person4, person1]
        actualSort = sortPeople.sort_by_birth_then_lastname()
        
        self.assertEqual(expectedSort, actualSort)
        
    def test_sort_by_last_name_desc(self):
        """
        Test sorting the people list by last name desc
        """
        person1 = Person("Bishop","Timothy", "Male","4/23/1967","Yellow")
        person2 = Person("Gerard","Neil", "Male","2/13/1943","Tan")
        person3 = Person("Abercrombie","Neil", "Male","2/13/1943","Tan")
        person4 = Person("Kelly","Sue", "Female","7/12/1959","Pink")
        peopleList = [person1, person2, person3, person4]
        
        sortPeople = SortPeople(peopleList)
        
        expectedSort = [person4, person2, person1, person3]
        actualSort = sortPeople.sort_by_last_name_desc()
        
        self.assertEqual(expectedSort, actualSort)
       

        
if __name__ == '__main__':
    unittest.main()