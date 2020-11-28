import csv
from datetime import datetime

october_file = open('october_database.csv')
csv_reader = csv.reader(october_file)

# count headcount

headcount=0
for row in csv_reader:
    _headcount = row[11]
    try:
        _headcount = int(_headcount)
    except ValueError:
        _headcount=0
    headcount += _headcount

now = datetime.now()
last_month = now.month -1 if now.month > 1 else 12
last_month_text = "January February March April May June July August September October November December".split()[last_month-1]

headcount_count = (f'''\n The headcount for {last_month_text} in ITIVITI is {headcount} active employees. \n''')
print (headcount_count)

#count VIE and show VIE

import pandas as pd

october_data = pd.read_csv('october_database.csv')

show_active_vie = f'''\n The active VIE for the month of {last_month_text} are: \n\n {(october_data.loc[(october_data["Contract type"] == "VIE") & (october_data['Contract status'] == 'Employed')])}'''

count_active_vie = f''' \n The active VIE for the month of {last_month_text} is number of ID's: \n\n {(october_data.loc[(october_data['Contract type'] == 'VIE') & (october_data['Contract status'] == 'Employed')]).count()}'''

print (show_active_vie)
print(count_active_vie)

#count and show interns

show_active_interns = f'''\n The active interns for the month of {last_month_text} are: \n\n {(october_data.loc[(october_data["Contract type"] == "Intern") & (october_data['Contract status'] == 'Employed')])}'''

count_active_interns = f''' \n The active interns for the month of {last_month_text} is number of ID's: \n\n {(october_data.loc[(october_data['Contract type'] == 'Intern') & (october_data['Contract status'] == 'Employed')]).count()}'''

print (show_active_interns)
print (count_active_interns)

#count and show consultants

show_active_consultants = f'''\n The active interns for the month of {last_month_text} are: \n\n {(october_data.loc[(october_data["Contract type"] == "Freelancer contract") & (october_data['Contract status'] == 'Employed')])}'''

count_active_consultants = f''' \n The active interns for the month of {last_month_text} is the number of ID's: \n\n {(october_data.loc[(october_data['Contract type'] == 'Freelancer contract') & (october_data['Contract status'] == 'Employed')]).count()}'''

print (show_active_consultants)
print (count_active_consultants)

#count and show new joiners

#count and show leavers



#mutable mapping str and repr methods

from collections.abc import MutableMapping, Mapping, Iterable, Collection, Container, Sized

class Departments(object):
    def __init__ (self, department):
        self.department = department
    def __repr__(self):
        return repr("Itiviti has the following department: " + self.department + " .")
    def __str__(self):
        return 'Itiviti has the following department : {self.department} .'.format(self=self)

class DepartmentsCollection:
    def __init__(self, departments_list = None):
        self.departments = list(departments_list) if managers_list else []
    def __iter__(self):
        return iter (self.departments)
    def __getitem__(self,index):
        return self.departments[index]

departments = [
    Departments('Legal'),
    Departments('Infrastructure'),
    Departments('G&A'),
    Departments('Professional Services'),
    Departments('Customer Succes'),
    Departments ('Global Markets'),
    Departments ('Product Strategy'),
    Departments ('Marketing')
]

print (departments)

class Managers():
    def __init__ (self, managers):
        self.managers = managers
    def __repr__(self):
        return repr("Itiviti has the following manager: " + self.managers + " .")
    def __str__(self):
        return 'Itiviti has the following manager : {self.managers} .'.format(self=self)

managers = [
    Managers ('Anil S.'),
    Managers ('Linda M'),
    Managers ('Karoline R.'),
    Managers ('Rob M.'),
    Managers ('Edouard R.'),
    Managers ('Peter T.'),
    Managers ('Ofir G.'),
    Managers ('Joshua M.'),
    Managers ('Antoine M.'),
]
print(managers)



#Inheritance

class ManagersStartYear(Managers):
    def __init__(self,managers,year):
        super().__init__(managers)
        self.year = year
    def __str__(self):
        return '{self.managers} has started in {self.year}. '.format(self=self)

manager_start_year = ManagersStartYear('Anil S.', 2019)
print (manager_start_year)

#Operator overloading


class SeniorityYear: 
    def __init__(self, year): 
        self.year = year
    def __gt__(self, other): 
        if(self.year>other.year): 
            return True
        else: 
            return False

employee_seniority_1 = SeniorityYear(2019) 
employee_seniority_2 = SeniorityYear(2020) 

if(employee_seniority_1>employee_seniority_2): 
    print("First seniority year is greater than second seniority year") 
else: 
    print("Second seniority year is greater than first seniority year")

#decorator

#sequence

itiviti_presence_countries_dict= {
    1: "Australia",
    2: "Brazil",
    3: "Canada",
    4: "France",
    5: "Hong Kong",
    6: "India",
    7: "Italy", 
    8: "Japan",
    9: "Philippines", 
    10: "Romania", 
    11: "Russia", 
    12: "Singapore", 
    13: "Sweden", 
    14: "United Kingdom",
    15: "United States"
}

def country_decorator(fnc):
    def wrapper():
        print (u'\U0001f310'+' \u2192')
        fnc()
    return wrapper

@country_decorator
def country_list():
    print ("Itiviti has offices in the following locations: ")
    for nr, country in itiviti_presence_countries_dict.items():
        print("{} {}".format(nr, country))

country_list()



