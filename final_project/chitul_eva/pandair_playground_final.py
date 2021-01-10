from pandair_application_final import Aircraft, QuickMaintenanceMixin, PassengerAircraft, PrivateAircraft, \
    CargoAircraft, CommercialAircraft, Airport, FleetDatabase, operate_flight, flights_log, generate_pairs, fleet_database_check, \
    flights_log_database, regional_fleet, AlterAircraft

#PLAYGROUND

# CREATE AIRCRAFT ALL TYPES

private_1 = PrivateAircraft('Bombardier', 300, 500, 200, 'P1000', 150, 5)
private_2 = PrivateAircraft('Airbus', 100, 200, 150, 'P2000', 50, 2)
private_3 = PrivateAircraft('Boeing', 800, 300, 150, 'P3000', 25, 8)
private_4 = PrivateAircraft('Bombardier', 200, 400, 190, 'P4000', 110, 7)

cargo_1 = CargoAircraft('Airbus', 1000, 700, 400, 'CA100', 1500, 25)
cargo_2 = CargoAircraft('Boeing', 2000, 1000, 800, 'CA200', 1500, 27)
cargo_3 = CargoAircraft('Boeing', 2000, 1000, 800, 'CA300', 1500, 30)
cargo_4 = CargoAircraft('Airbus', 1500, 800, 900, 'CA400', 1000, 20)

commercial_1 = CommercialAircraft('Airbus', 1000, 900, 800, 'CO100', 30, 80)
commercial_2 = CommercialAircraft('Airbus', 1000, 900, 800, 'CO200', 30, 350)
commercial_3 = CommercialAircraft('Bombardier', 800, 600, 400, 'CO300', 20, 200)
commercial_4 = CommercialAircraft('Boeing', 900, 800, 600, 'CO400', 25, 250)

print(private_1)
print(private_2)
print(cargo_1)
print(cargo_2)
print(commercial_1)
print(commercial_2)

# CHECK DUE FOR MAINTENANCE

print(commercial_4.due_for_maintenance())
print(commercial_2.due_for_maintenance())
print(private_1.due_for_maintenance())
print(cargo_3.due_for_maintenance())
print(private_2.due_for_maintenance())


# CHECK QUICK MAINTENANCE

print('Private 3 before quick maintenance', private_3.number_flights_maintenance)
print('Cargo 2 before quick maintenance', cargo_2.number_flights_maintenance, '\n')

print(private_3.quick_maintenance())
print(cargo_2.quick_maintenance(), '\n')

print('Private 3 after quick maintenance', private_3.number_flights_maintenance)
print('Cargo 2 after quick maintenance', cargo_2.number_flights_maintenance, '\n')

print(private_1.quick_maintenance())
print(cargo_1.quick_maintenance(), '\n')

# CREATE AIRPORT, ADD/REMOVE AIRCRAFT FROM AIRPORT

brussels_airport = Airport()
brussels_airport.add_aircraft(commercial_2)
brussels_airport.add_aircraft(private_2)
brussels_airport.add_aircraft(cargo_3)
brussels_airport.add_aircraft(cargo_3)

cluj_airport = Airport()
cluj_airport.add_aircraft(commercial_1)
cluj_airport.add_aircraft(private_2)
cluj_airport.add_aircraft(private_1)
cluj_airport.add_aircraft(cargo_1)

berlin_airport = Airport()
berlin_airport.add_aircraft(private_3)
berlin_airport.add_aircraft(cargo_2)
berlin_airport.add_aircraft(cargo_1)
berlin_airport.add_aircraft(cargo_3)

prague_airport = Airport()
prague_airport.add_aircraft(private_4)
prague_airport.add_aircraft(cargo_4)
prague_airport.add_aircraft(commercial_3)
prague_airport.add_aircraft(commercial_4)

print('Brussels', brussels_airport, '\n')
print('Cluj-Napoca', cluj_airport, '\n')
print('Berlin', berlin_airport, '\n')
print('Prague', prague_airport, '\n')

brussels_airport.remove_aircraft(cargo_3)
cluj_airport.remove_aircraft(commercial_1)
berlin_airport.remove_aircraft(cargo_3)
prague_airport.remove_aircraft(private_4)

print('Brussels', brussels_airport, '\n')
print('Cluj-Napoca', cluj_airport, '\n')
print('Berlin', berlin_airport, '\n')
print('Prague', prague_airport, '\n')

# ADD TWO AIRPORTS - OPERATION OVERLOAD CHECK

print(brussels_airport)
print(berlin_airport)
print('Regional', brussels_airport+berlin_airport)
print('Regional', prague_airport+berlin_airport)

# CREATE FLEET, ADD/REMOVE AIRPORTS FROM FLEET

fleet_database = FleetDatabase()

print(fleet_database, '\n')
fleet_database.add_airport('Brussels', brussels_airport)
fleet_database.add_airport('Cluj-Napoca', cluj_airport)
fleet_database.add_airport('Berlin', berlin_airport)
fleet_database.add_airport('Prague', prague_airport)
print(fleet_database, '\n')

print(fleet_database_check)
fleet_database.remove_airport('brussels')
print(fleet_database, '\n')
print(fleet_database_check, '\n')

# OPERATE FLIGHT & DECORATOR

operate_flight(fleet_database, 'Brussels', 'Berlin', commercial_2)
print(fleet_database, '\n')

operate_flight(fleet_database, 'Berlin', 'Cocomo', private_3)
print(fleet_database, '\n')

operate_flight(fleet_database, 'Brussels', 'Munich', private_2)
print(fleet_database, '\n')

operate_flight(fleet_database, 'Prague', 'Munich', cargo_4)
print(fleet_database, '\n')

print(flights_log_database)


# GENERATOR AND GENERATE PAIRS

check = generate_pairs(fleet_database)

for pair in generate_pairs(fleet_database):
    print(next(check))

print(fleet_database, '\n')

# CONTEXT MANAGER AND ALTERING DUE FOR MAINTENANCE METHOD

aircraft = PrivateAircraft('Bombardier', 300, 500, 200, 'P1000', 150, 100)

with AlterAircraft(aircraft) as check_altered_aircraft:
    print(f'Altered due for maintenance for {aircraft} with {aircraft.number_flights_maintenance} flights returning', check_altered_aircraft.due_for_maintenance())

print(f'Altered due for maintenance for {aircraft} with {aircraft.number_flights_maintenance} flights returning', check_altered_aircraft.due_for_maintenance())
