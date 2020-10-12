dataset = [
	('Belgium', 2017, 'M', 1.8),
	('Belgium', 2018, 'M', 2.0),
	('Bulgaria', 2017, 'M', 1.8),
	('Bulgaria', 2018, 'M', 1.5),
	('Czechia', 2017, 'M', 2.1),
	('Czechia', 2018, 'M', 2.3),
	('Denmark', 2017, 'M', 3.3),
	('Denmark', 2018, 'M', 2.5),
	('Germany', 2017, 'M', 2.6),
	('Germany', 2018, 'M', 2.5),
	('Estonia', 2017, 'M', 3.6),
	('Estonia', 2018, 'M', 4.7),
	('Latvia', 2017, 'M', 5.0),
	('Latvia', 2018, 'M', 3.1),
	('Serbia', 2017, 'M', 5.3),
	('Serbia', 2018, 'M', 3.7),
	('Romania', 2017, 'M', 0.4),
	('Romania', 2018, 'M', 0.5),
	('Belgium', 2017, 'F', 2.3),
	('Belgium', 2018, 'F', 2.5),
	('Bulgaria', 2017, 'F', 1.8),
	('Bulgaria', 2018, 'F', 1.5),
	('Czechia', 2017, 'F', 1.7),
	('Czechia', 2018, 'F', 1.8),
	('Denmark', 2017, 'F', 2.7),
	('Denmark', 2018, 'F', 3.0),
	('Germany', 2017, 'F', 2.9),
	('Germany', 2018, 'F', 2.5),
	('Estonia', 2017, 'F', 4.3),
	('Estonia', 2018, 'F', 4.4),
	('Latvia', 2017, 'F', 6.3),
	('Latvia', 2018, 'F', 4.3),
	('Serbia', 2017, 'F', 4.7),
	('Serbia', 2018, 'F', 3.7),
	('Romania', 2017, 'F', 0.5),
	('Romania', 2018, 'F', 0.4)
]
list = [1, 2, 3, 4]
health_index_2017 = {
    country + sex:[sex, health_index] for country, _, sex, health_index in dataset if _==2017
}
health_index_2018 = {
    country + sex:[sex, health_index] for country, _, sex, health_index in dataset if _==2018 and sex == 'M'
}
#print(health_index_2017)
#print(health_index_2018)
germany = {
    str(year) + sex:[sex, health_index] for _, year, sex, health_index in dataset
}
#print(germany)
health_index = {
    country + '_' + str(year) + sex:[year, sex, health_index] for country, year, sex, health_index in dataset
}
#print(health_index)
for key in health_index:
    if health_index[key][2]>5:
        print(health_index[key])
        
for key in health_index:
    if health_index[key][2]>5 and health_index[key][1] == 'F':
        print(health_index[key])
        
for key in health_index:
    print(health_index[key])