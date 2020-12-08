from application import headcount, departments

import unittest

def test_headcount(self):
    if isinstance (headcount, str) == "True" and isinstance (headcount,int) == "False":
        print ('The output is incorrect: headcount should not be a string')
    else:
        print ("The outcput is correct: headcount is an integer")

test_headcount(headcount)

def test_departments(self):
    if len(departments) == 8:
        print ("\nThe departments number from the database is correct\n")
    else:
        print ("\nThe number of departments from the database is incorrect\n")

test_departments(departments)