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

count_active_consultants = f''' \n The active interns for the month of {last_month_text} is number of ID's: \n\n {(october_data.loc[(october_data['Contract type'] == 'Freelancer contract') & (october_data['Contract status'] == 'Employed')]).count()}'''

print (show_active_consultants)
print (count_active_consultants)









