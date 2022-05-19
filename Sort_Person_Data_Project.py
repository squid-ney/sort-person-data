#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:52:13 2022

@author: Sydney
"""
import Person

# Sorts
def sort_last_name(people, reverse=False):
    def sort_key(person):
        return person.lastName
    people.sort(key=sort_key, reverse=reverse)
    return people

def sort_birth_date(people):
    def sort_key(person):
        return person.dateOfBirth
    people.sort(key=sort_key)
    return people
  
def sort_by_gender_then_lastname(people):
    females = []
    males = []

    for person in people:
        if person.gender == "Female":
            females.append(person)
        if person.gender == "Male":
            males.append(person)  
    
    femalesByLastName = sort_last_name(females)
    malesByLastName = sort_last_name(males)
    sortedByGenderAndLastName = femalesByLastName + malesByLastName
    return sortedByGenderAndLastName

def sort_by_birth_then_lastname(people):
    peopleByLastName = sort_last_name(people)
    sortedByBirthDateAndLastName = sort_birth_date(peopleByLastName)
    return sortedByBirthDateAndLastName

def sort_by_last_name_desc(people):
    reverse = True
    return sort_last_name(people, reverse)





def pre_process_data(data): 
    def get_deliminator(data):
        if "," in data[0]:
            return ", "
        elif "|" in data[0]:
            return " | "
        else:
            return " "
    
    def remove_middle_initial(personData):
        personData.pop(2)
        
    def format_gender(personData):
        gender = personData[2] 
        if gender == 'F':
            personData[2] = "Female"
        else:
            personData[2] = "Male" 
        return personData
    
    def format_birth_date(personData):
        birthDate = personData[4]
        personData[4] = birthDate.replace('-','/')
        return personData
        
    def swap_color_and_birth_date(personData):
        color = personData[3]
        birthDate = personData[4]
        personData[3] = birthDate
        personData[4] = color
        return personData
            
    people = []
    deliminator = get_deliminator(data)
    for personString in data:
        personData = personString.strip().split(deliminator)
        if deliminator == " | ":
            remove_middle_initial(personData)
            personData = format_birth_date(personData)
            personData = format_gender(personData)
            personData = swap_color_and_birth_date(personData)
        elif deliminator == " ":
            remove_middle_initial(personData)
            personData = format_birth_date(personData)
            personData = format_gender(personData)
        else:
            personData = swap_color_and_birth_date(personData)
            
        people.append(Person.Person(personData[0], personData[1], personData[2], personData[3], personData[4]))
    return people  
    


def read_file():
    lines = []
    with open('def-method-code-test-input-files/comma.txt') as f:
        lines = f.readlines()
        f.close()
    return lines

def print_list_of_people_objets(people):
    for person in people:
        person.printPerson()
        
def print_sort(label, people, newLine=True):
    print(label)
    print_list_of_people_objets(people)
    if newLine:
        print()

def sort_people_data():
   data = read_file()
   people = pre_process_data(data)
   print_sort("Output 1:", sort_by_gender_then_lastname(people))
   print_sort("Output 2:", sort_by_birth_then_lastname(people))
   print_sort("Output 3:", sort_by_last_name_desc(people), False)
                 
    
sort_people_data()
    
    
    