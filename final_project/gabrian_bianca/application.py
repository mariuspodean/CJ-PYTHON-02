import csv
from datetime import datetime

october_file = open('october_database.csv')
csv_reader = csv.reader(october_file)

headcount = 0
for row in csv_reader:
    _headcount = row[11]
    try:
        _headcount = int(_headcount)
    except ValueError:
        _headcount = 0
    headcount += _headcount

now = datetime.now()
last_month = now.month - 1 if now.month > 1 else 12
last_month_text = "January February March April May June July August September October November December".split(
)[last_month - 1]

headcount_count = (
    f'''\n The headcount for {last_month_text} in ITIVITI is {headcount} active employees. \n'''
)

import pandas as pd

october_data = pd.read_csv('october_database.csv')

show_active_vie = f'''\n\n The active VIE for the month of {last_month_text} are: \n\n {(october_data.loc[(october_data["Contract type"] == "VIE") & (october_data['Contract status'] == 'Employed')])}'''

count_active_vie = f''' \n The active VIE for the month of {last_month_text} is number of ID's: \n\n {(october_data.loc[(october_data['Contract type'] == 'VIE') & (october_data['Contract status'] == 'Employed')]).count()}'''

show_active_interns = f'''\n\n The active interns for the month of {last_month_text} are: \n\n {(october_data.loc[(october_data["Contract type"] == "Intern") & (october_data['Contract status'] == 'Employed')])}'''

count_active_interns = f''' \n The active interns for the month of {last_month_text} is number of ID's: \n\n {(october_data.loc[(october_data['Contract type'] == 'Intern') & (october_data['Contract status'] == 'Employed')]).count()}'''

show_active_consultants = f'''\n\n The active interns for the month of {last_month_text} are: \n\n {(october_data.loc[(october_data["Contract type"] == "Freelancer contract") & (october_data['Contract status'] == 'Employed')])}'''

count_active_consultants = f''' \n The active interns for the month of {last_month_text} is the number of ID's: \n\n {(october_data.loc[(october_data['Contract type'] == 'Freelancer contract') & (october_data['Contract status'] == 'Employed')]).count()}'''


class OutputOctober(object):
    def __init__(self, october_database_output):
        self.october_database_output = october_database_output

    def __enter__(self):
        self.october_database_output = open(self.october_database_output, 'w')
        return self.october_database_output

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
            return True


from collections.abc import MutableMapping, Mapping, Iterable, Collection, Container, Sized


class Departments(object):
    def __init__(self, department):
        self.department = department

    def __repr__(self):
        return repr("Itiviti has the following department: " +
                    self.department + " .")

    def __str__(self):
        return 'Itiviti has the following department : {self.department} .'.format(
            self=self)


class DepartmentsCollection:
    def __init__(self, departments_list=None):
        self.departments = list(departments_list) if managers_list else []

    def __iter__(self):
        return iter(self.departments)

    def __getitem__(self, index):
        return self.departments[index]


departments = [
    Departments('Legal'),
    Departments('Infrastructure'),
    Departments('G&A'),
    Departments('Professional Services'),
    Departments('Customer Succes'),
    Departments('Global Markets'),
    Departments('Product Strategy'),
    Departments('Marketing')
]


class Managers():
    def __init__(self, managers):
        self.managers = managers

    def __repr__(self):
        return repr("Itiviti has the following manager: " + self.managers +
                    " .")

    def __str__(self):
        return 'Itiviti has the following manager : {self.managers} .'.format(
            self=self)


managers = [
    Managers('Anil S.'),
    Managers('Linda M'),
    Managers('Karoline R.'),
    Managers('Rob M.'),
    Managers('Edouard R.'),
    Managers('Peter T.'),
    Managers('Ofir G.'),
    Managers('Joshua M.'),
    Managers('Antoine M.'),
]


class ManagersStartYear(Managers):
    def __init__(self, managers, year):
        super().__init__(managers)
        self.year = year

    def __str__(self):
        return '{self.managers} has started in {self.year}. '.format(self=self)


manager_start_year = ManagersStartYear('Anil S.', 2019)


class SeniorityYear:
    def __init__(self, year):
        self.year = year

    def __gt__(self, other):
        if (self.year > other.year):
            return True
        else:
            return False


itiviti_presence_countries_dict = {
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
        print(u'\U0001f310' + ' \u2192')
        fnc()

    return wrapper


@country_decorator
def country_list():
    print("Itiviti has offices in the following locations: ")
    for nr, country in itiviti_presence_countries_dict.items():
        print("{} {}".format(nr, country))


class EmployeeNmae:
    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name


class DefaultRecord(EmployeeNmae):
    def __init__(self):
        self.name = "No employee record"


def EmployeeDataGenerator():
    file = "october_database.csv"
    for row in open(file, encoding="ISO-8859-1"):
        yield row


import logging

logging.basicConfig(filename='logging_file', level=logging.DEBUG)
