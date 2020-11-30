dataset = [('Belgium', 2017, 'M', 1.8), ('Germany', 2017, 'M', 2.6),
 ('Spain', 2017, 'M', 1.2), ('France', 2017, 'M', 3.2),
 ('Austria', 2017, 'M', 1.8), ('Latvia', 2017,'M', 5.0),
 ('Luxembourg', 2017, 'M', 4.2), ('Turkey', 2017, 'M', 3.3),
 ('Belgium', 2018, 'M', 2.0), ('Germany', 2018, 'M', 2.5),
 ('Spain', 2018, 'M', 1.2), ('France', 2018, 'M', 2.8),
 ('Latvia', 2018, 'M', 5.0), ('Luxembourg', 2018, 'M', 4.1),
 ('Austria', 2018, 'M', 2.1), ('Turkey', 2018, 'M', 3.5),
 ('Belgium', 2017, 'F', 2.3), ('Germany', 2017, 'F', 2.9),
 ('Spain', 2017, 'F', 1.3), ('France', 2017, 'F', 4.3),
 ('Latvia', 2017, 'F', 6.3), ('Luxembourg', 2017, 'F', 4.1),
 ('Austria', 2017, 'F', 2.4), ('Turkey', 2017, 'F', 4.4),
 ('Belgium', 2018, 'F', 2.5), ('Germany', 2018, 'F', 2.5),
 ('Spain', 2018, 'F', 2.0), ('France', 2018, 'F', 4.3),
 ('Latvia', 2018, 'F', 4.3), ('Luxembourg', 2018, 'F', 5.3),
 ('Austria', 2018, 'F', 2.2), ('Turkey', 2018, 'F', 5.6)]
print (dataset)
health_index_2017 = {
	country : [sex, health_index]
		for country, year, sex, health_index in dataset
		if year == 2017
}
print (health_index_2017)
 
health_index_2018 = {
        country : [sex, health_index]
                for country, year, sex, health_index in dataset
                if year == 2018
}
print (health_index_2018)

germany = {
	year: [sex, health_index]
		for country, year, sex, health_index in dataset
		if country == 'Germany'
}
print (germany)

health_index = {
	country + '_' + str(year): [year, sex, health_index]
		for country, year, sex, health_index in dataset
}
print (health_index)

health_index = {
	country + '_' + str(year): [year, sex, health_index]
                for country, year, sex, health_index in dataset
		if health_index > 5
}
print (health_index)

health_index = {
        country + '_' + str(year): [year, sex, health_index]
                for country, year, sex, health_index in dataset
                if health_index > 5
		if sex == 'F'
}
print (health_index)

health_index_values = health_index.values()
for year, sex, health_index in health_index_values:
 print (health_index)


