from collections.abc import Iterable, Collection, Mapping

sheet = [
    ('Belgium',2017,'M',1.8),
    ('Spain',2017,'F',1.3),
    ('Romania',2017,'M',0.4),
    ('Germany',2017,'F',2.9),
    ('Greece',2018,'F',2.0),
    ('Germany',2018,'M',2.5)
    
    ]

health_index_2017 = {
     country:[sex,health_index]
    for country,_, sex, health_index in sheet if _ == 2017 
    }
print(f'\nIndex for 2017 is:',health_index_2017)

health_index_2018 = {
     country:[sex,health_index]
    for country,_, sex, health_index in sheet if _ == 2018
    }
print(f'\nIndex for 2018 is:',health_index_2018)

germany = {
    year:[sex,health_index]
    for _,year,sex, health_index in sheet if _ == 'Germany'
    }
print(f'\nIndex for Germany by year is:',germany)

health_index = {
    country+'_'+str(year):[year,sex,health_index]
    for country,year,sex,health_index in sheet
    }
print(f'\nHealth_Index dictionary',health_index)

# create a loop to print the HealthIndex
values = health_index.values()
list_values = list(values)
print(f'\nValues: ',list_values)
above_dict = [
        index
        for _,_,index in values if index
        ]
print(f'\nLoop to print the health index',above_dict)

    
