# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:49:06 2024

@author: Lenovo
"""

#object built in python object  class
class Person(object):
    def __init__(self, family_name, first_name):
        self.family_name = family_name
        self.first_name = first_name 

    def familyName(self):
        return self.family_name

    def firstName(self):
        return self.first_name

    # def __cmp__(self, other):
    #     return cmp((self.family_name, self.first_name),
    #                (other.family_name, other.first_name))

    def __str__(self):
        return f'<Person: {self.first_name} {self.family_name}>'

    def say(self, toWhom, something):
        return f'{self.first_name} {self.family_name} says to {toWhom}: {something}'

    def sing(self, toWhom, something):
        return self.say(toWhom, something + ' tra la la')
