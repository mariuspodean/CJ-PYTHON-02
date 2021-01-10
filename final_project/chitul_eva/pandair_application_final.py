import itertools
import logging
import time
import datetime

fleet_database_check = set()
flights_log_database = {}
regional_fleet = {}

logging.basicConfig(level=logging.DEBUG, filename=f'{datetime.date.today()}_pandair_logging')
log = logging.getLogger('Pandair Airline')


class Aircraft:

    def __init__(self, manufacturer, weight, speed, consumption, identifier, number_flights_maintenance):
        self.manufacturer = manufacturer
        self.weight = weight
        self.speed = speed
        self.consumption = consumption
        self.identifier = identifier
        self.number_flights_maintenance = number_flights_maintenance

    def __str__(self):
        return f'Aircraft type {type(self).__name__}, identifier {self.identifier}, manufacturer {self.manufacturer}'

    def __repr__(self):
        return self.identifier

    def due_for_maintenance(self):

        log.info(f' Checking if Aircraft {self.identifier} is due for maintenance')
        if self.number_flights_maintenance >= 30:
            return True
        else:
            return False


class QuickMaintenanceMixin:

    def quick_maintenance(self):

        if self.number_flights_maintenance - 10 < 0:
            self.number_flights_maintenance = 0
        else:
            self.number_flights_maintenance -= 10

        log.debug(f'{time.asctime(time.localtime(time.time()))} {self} completed quick maintenance. Flights number is now {self.number_flights_maintenance}')
        return f'{self} has gone through quick maintenance. Flights number is now: {self.number_flights_maintenance}'


class PassengerAircraft(Aircraft):

    def __init__(self, manufacturer, weight, speed, consumption, identifier, number_flights_maintenance, number_passengers):
        self.number_passengers = number_passengers
        super().__init__(manufacturer, weight, speed, consumption, identifier, number_flights_maintenance)


class CargoAircraft(Aircraft, QuickMaintenanceMixin):

    def __init__(self, manufacturer, weight, speed, consumption, identifier, load_weight, number_flights_maintenance):
        self.load_weight = load_weight
        super().__init__(manufacturer, weight, speed, consumption, identifier, number_flights_maintenance)

    def due_for_maintenance(self):
        if self.number_flights_maintenance >= 50:
            return True
        else:
            return False


class PrivateAircraft(PassengerAircraft, QuickMaintenanceMixin):

    def __init__(self, manufacturer, weight, speed, consumption, identifier, number_passengers, number_flights_maintenance):
        super().__init__(manufacturer, weight, speed, consumption, identifier, number_flights_maintenance, number_passengers)


class CommercialAircraft(PassengerAircraft):

    def __init__(self, manufacturer, weight, speed, consumption, identifier, number_flights_maintenance, number_passengers):
        super().__init__(manufacturer, weight, speed, consumption, identifier, number_flights_maintenance, number_passengers)


class Airport:

    def __init__(self):
        self.airport_list = []

    def __len__(self):
        return len(self.airport_list)

    def __getitem__(self, index):
        return self.airport_list[index]

    def __str__(self):
        return f'Airport: {self.airport_list}'

    def __repr__(self):
        return f'{self.airport_list}'

    def __add__(self, second_airport):
        region_airport = Airport()
        all_aircraft = self.airport_list + second_airport.airport_list
        for aircraft in all_aircraft:
            region_airport.add_aircraft(aircraft, check_duplicates=False)
        log.debug(f'{time.asctime(time.localtime(time.time()))} Created Regional Airport from {self} and {second_airport}')
        return region_airport

    def add_aircraft(self, aircraft, check_duplicates=True):

        if aircraft in fleet_database_check and check_duplicates:
            print(f'{aircraft} already in Fleet. Cannot duplicate \n')
            log.info(f' {aircraft} already in Fleet.')
        else:
            self.airport_list.append(aircraft)
            fleet_database_check.add(aircraft)
            log.debug(f'{time.asctime(time.localtime(time.time()))} {aircraft} added in Airport and Fleet. Airplanes in fleet overview: {fleet_database_check}')

    def remove_aircraft(self, aircraft):
        if aircraft in self.airport_list:
            position = self.airport_list.index(aircraft)
            del self.airport_list[position]
            fleet_database_check.remove(aircraft)
            log.debug(f'{time.asctime(time.localtime(time.time()))} {aircraft} removed from Airport and Fleet. Airplanes in fleet overview: {fleet_database_check}')
        else:
            print(f'{aircraft} not found at Airport. Unable to remove')
            log.info(f' {aircraft} not found at Airport.')


class FleetDatabase:

    def __init__(self):
        self.fleet = {}

    def __getitem__(self, key):
        if key not in self.fleet:
            print(f'Airport {key} not in Fleet Database. Airport will be added')
            log.info(f' Airport {key} not in Fleet Database.')
            self.fleet[key] = Airport()
            log.debug(f'{time.asctime(time.localtime(time.time()))} Airport {key} not found. Airport was added to Fleet Database. Fleet Overview: {self.fleet}')
        return self.fleet[key]

    def __delitem__(self, key):
        del self.fleet[key]

    def __setitem__(self, key, value):
        self.fleet[key] = value

    def __len__(self):
        return len(self.fleet)

    def __iter__(self):
        return iter(self.fleet)

    def __str__(self):
        return f'Fleet and Location Overview: {self.fleet}'

    def __repr__(self):
        return f'{self.fleet}'

    def add_airport(self, airport_name, airport_list):
        if airport_name.title() in self.fleet.keys():
            print('Airport already in Fleet Database. The new aircrafts will replace the old ones')
            log.info(f' {airport_name.title()} already in Fleet Database.')
            for aircraft in self.fleet[airport_name.title()]:
                fleet_database_check.remove(aircraft)
                log.debug(f'{time.asctime(time.localtime(time.time()))} {airport_name} removed from Fleet Database. Fleet Overview {fleet_database_check}')

        for new_aircraft in airport_list:
            fleet_database_check.add(new_aircraft)
            log.debug(f'{time.asctime(time.localtime(time.time()))} {new_aircraft} added to Fleet Database. Fleet Overview {fleet_database_check}')

        self.fleet[airport_name.title()] = airport_list
        log.debug(f'{time.asctime(time.localtime(time.time()))} {airport_name.title()} fleet replaced. New {airport_name.title()} {airport_list} ')

    def remove_airport(self, airport_name):
        if airport_name.title() in self.fleet.keys():
            for aircraft in self.fleet[airport_name.title()]:
                fleet_database_check.remove(aircraft)
                log.debug(f'{time.asctime(time.localtime(time.time()))} {aircraft} removed from Fleet Database. Fleet overview {fleet_database_check}')
            del self.fleet[airport_name.title()]
            log.debug(f'{time.asctime(time.localtime(time.time()))} {airport_name.title()} removed from Fleet Database. Overview of airports {self.fleet}')
        else:
            print(f'{airport_name.title()} Airport not found in Fleet Database. Unable to remove')
            log.info(f' {airport_name.title()} not found in Fleet. ')


def flights_log(flight):

    def track_flight(*args):
        results = flight(*args)
        if results:
            aircraft, city, destination = results[0], results[1], results[2]

            flights_log_database[f'Entry {len(flights_log_database) + 1}'] = f' Aircraft {aircraft.identifier}: {city} to {destination}'
            log.info(f' New flight added to flight log: {aircraft.identifier}: {city} to {destination}')

            if aircraft.due_for_maintenance:
                print(f'Alert: Aircraft {aircraft.identifier} is due for maintenance!')
                log.info(f' Aircraft Alert: {aircraft.identifier} is due for maintenance!')
        else:
            return None

        return flight
    return track_flight


@flights_log
def operate_flight(fleet_data, city, destination, aircraft):

    if aircraft in fleet_data[city.title()]:

        fleet_data[city.title()].remove_aircraft(aircraft)
        log.debug(f'{time.asctime(time.localtime(time.time()))} {aircraft} removed from {city.title()} airport. {city.title()} airport overview: {fleet_data[city.title()]}')

        fleet_data[destination.title()].add_aircraft(aircraft)
        log.debug(f'{time.asctime(time.localtime(time.time()))} {aircraft} added to {destination} airport. {destination.title()} airport overview: {fleet_data[destination.title()]}')

        aircraft.number_flights_maintenance += 1
        log.debug(f'{time.asctime(time.localtime(time.time()))} {aircraft} number of flights increased by 1. Number of flights operated now at {aircraft.number_flights_maintenance}')

    else:
        print(f'{aircraft} not in {city}. Cannot perform flight ')
        log.info(f' {aircraft} not found in {city} airport.')
        return None

    return aircraft, city, destination


def generate_pairs(fleet_database):

    list_origin = set([origin for origin, fleet in fleet_database.fleet.items() for aircraft in fleet
                   if isinstance(aircraft, PassengerAircraft) and aircraft.number_passengers > 100])

    list_destination = set([destination for destination, planes in fleet_database.fleet.items() if len(planes) <= 3])

    print(list_origin)
    print(list_destination)

    for origin, destination in itertools.product(list_origin, list_destination):
        if origin != destination:
            log.debug(f'{time.asctime(time.localtime(time.time()))} New origin-destination pair was generated: {origin} - {destination}')
            yield f'Possible origin destination pair: {origin} - {destination}'


class AlterAircraft:

    def __init__(self, plane):
        self.plane = plane

    def __enter__(self):
        self.pandair_status = open('pandair_status.txt', 'w')
        self.pandair_status.write('Altering behaviour of due for maintenance method. Be careful with the flights! \n')

        self.original_maintenance_method = self.plane.due_for_maintenance
        self.plane.due_for_maintenance = lambda: False

        log.info(f'Behaviour of {self.plane} has been changed')
        log.debug(f'{time.asctime(time.localtime(time.time()))} Due for maintenance method for {self.plane} now returning {self.plane.due_for_maintenance}')

        return self.plane

    def __exit__(self, exc_type, exc_value, traceback):
        self.pandair_status.write(f'Due for maintenance method of aircraft returned to original state\n')
        self.pandair_status.write('Closing down Pandair App. Travel safe!\n')

        self.plane.due_for_maintenance = self.original_maintenance_method

        log.info(f'Behaviour of {self.plane} has returned to original')
        log.debug(f'{time.asctime(time.localtime(time.time()))} Due for maintenance method for {self.plane} now back to original form')

