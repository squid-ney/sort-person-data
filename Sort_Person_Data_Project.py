#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:52:13 2022

@author: Sydney
"""

# Helpers
def sort_last_name(items, reverse=False):
    def sort_key(person):
        return person[0]
    items.sort(key=sort_key, reverse=reverse)
    return items

def sort_birth_date(items):
    def sort_key(person):
        return person[4]
    items.sort(key=sort_key)
    return items
  
def print_sorted_list(prefix, people, newLine=True):
    print(prefix)
    for person in people:
        print(' '.join(person))
    if newLine:
        print()
        
def read_file():
    lines = []
    with open('def-method-code-test-input-files/comma.txt') as f:
        lines = f.readlines()
        f.close()
    return lines

def split_by_deliminator(deliminator, lines):
    people = []
    for line in lines:
        people.append(line.strip().split(deliminator))
    return people   
    
    

# Sorts
def sort_by_gender_then_lastname(people):
    females = []
    males = []

    for person in people:
        if person[2] == "Female" or person[2] == "F":
            females.append(person)
        if person[2] == "Male" or person[2] == "M":
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




# Pre Processing
def parse_comma_deliminator(listOfText):
    people = split_by_deliminator(", ", listOfText)
    for person in people:
        color = person[3]
        birthDate = person[4]
        person[3] = birthDate
        person[4] = color
    return people

def parse_space_deliminator(listOfText):
    people = split_by_deliminator(" ", listOfText)
    for person in people:
        birthDate = person[4]
        person[4] = birthDate.replace('-','/')
        person.pop(2)
    return people

def parse_pipe_deliminator(listOfText):
    people = split_by_deliminator(" | ", listOfText)
    for person in people:
        color = person[4]
        birthDate = person[5]
        person[4] = birthDate.replace('-','/')
        person[5] = color
        person.pop(2)
    return people

def parse_text(listOfText):
    if "," in listOfText[0]:
        return parse_comma_deliminator(listOfText)
    elif "|" in listOfText[0]:
        return parse_pipe_deliminator(listOfText)
    else:
        return parse_space_deliminator(listOfText)

    

def sort_code_challenge():
   listOfText = read_file()
   people = parse_text(listOfText)
   
   print_sorted_list("Output 1:", sort_by_gender_then_lastname(people))
   print_sorted_list("Output 2:", sort_by_birth_then_lastname(people))
   print_sorted_list("Output 3:", sort_by_last_name_desc(people), False)
       
            
    
sort_code_challenge()
    
    