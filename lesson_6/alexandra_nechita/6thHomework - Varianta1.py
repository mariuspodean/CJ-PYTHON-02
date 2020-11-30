#Varianta 1 - with no use of the description list

from collections import defaultdict
import math

# function that prepares the dataset

def prepare_dataset (raw_data):
    description = ['Country', ('2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ', '2019 ')]
    dataset_dict = defaultdict (list) 
    for country, coverage in raw_data:
        for year, index in enumerate(coverage, start=2011):
            dataset_dict[country].append ({'year':year, 'coverage':index})
    return dataset_dict

# function to retrieve data for each year

def get_year_data (dataset_dict, required_year):
    year_data_dict = defaultdict (list)
    for country, data_per_country in dataset_dict.items():
        for data_per_year in data_per_country:
            if int(data_per_year['year'])==required_year:
                year_data_dict[required_year].append((country, data_per_year['coverage']))
    return year_data_dict

# function to retrieve data for each country

def get_country_data (dataset_dict, required_country):
    country_data_dict = defaultdict (list)
    for country, data_per_country in dataset_dict.items():
        if country==required_country:
            for data_per_year in data_per_country:            
                country_data_dict[required_country].append((data_per_year['year'], data_per_year['coverage']))
    return country_data_dict

# function to perform average from an iterable(of year data or country data)
# Varianta 1 - where we skip non-numeric data for coverage

def clean_up(coverage_list):
    new_coverage_list=[]
    for country_or_year, coverage in coverage_list:
        coverage = coverage.replace(" ","")
        if coverage.isdigit():
            new_coverage_list.append(int(coverage))
    return new_coverage_list
        
        
def perform_average(coverage_list):
    new_coverage_list = clean_up(coverage_list)
    if len(new_coverage_list):
        suma= sum(new_coverage_list)
        return float(suma/len(new_coverage_list))
    else:
        print('We have no data to perform the average')
        return 0

raw_data = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', ': ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
    ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
    ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ', '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
]

print('The whole dataset is: ', dict(prepare_dataset(raw_data)), '\n')

dataset_dict = prepare_dataset(raw_data)
print('get_year_data is: ', dict(get_year_data(dataset_dict, 2019)), '\n')
print('get_country_data is: ', dict(get_country_data(dataset_dict, 'RO')), '\n')

coverage_per_country=get_country_data(dataset_dict, 'AL')
coverage_per_year=get_year_data(dataset_dict, 2019)

print ('Average per country is: ', perform_average(coverage_per_country['AL']))
print ('Average per year is: ', perform_average(coverage_per_year[2019]))

