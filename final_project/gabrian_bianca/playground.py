from application import headcount, headcount_count, show_active_vie, count_active_vie, show_active_interns, count_active_interns, show_active_consultants, count_active_consultants, OutputOctober, Departments, DepartmentsCollection, departments, Managers, managers, ManagersStartYear, manager_start_year, SeniorityYear, country_list, DefaultRecord, EmployeeDataGenerator, logging

print (headcount)

print (headcount_count)

print (show_active_vie)

print(count_active_vie)

print (show_active_interns)

print (count_active_interns)

print (show_active_consultants)

print (count_active_consultants)

with OutputOctober('october_database_output.csv') as opened_file:
    opened_file.write(headcount_count + show_active_vie + show_active_interns + show_active_consultants)

print (departments)

print(managers)

manager_start_year = ManagersStartYear('Anil S.', 2019)
print (manager_start_year)

employee_seniority_1 = SeniorityYear(2019) 
employee_seniority_2 = SeniorityYear(2020) 

if(employee_seniority_1>employee_seniority_2): 
    print("First seniority year is greater than second seniority year") 
else: 
    print("Second seniority year is greater than first seniority year")

country_list()

employee_record = DefaultRecord()

employee_name = employee_record.getname()

print(employee_name)

employee_record.setname("Bianca Gabrian")

employee_name = employee_record.getname()

print (employee_name)

data_generator = EmployeeDataGenerator()

print(next(data_generator))

print(next(data_generator))

print(next(data_generator))

print(next(data_generator))

logging.debug (departments)

logging.debug (managers)

logging.debug (manager_start_year)


