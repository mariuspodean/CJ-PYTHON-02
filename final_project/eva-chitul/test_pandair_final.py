from final_project.eva-chitul import pandair_application_final
import unittest


class AircraftCreation(unittest.TestCase):

    def test_private_aircraft_creation(self):

        arguments = ['Boeing', 100, 200, 150, 'P000', 100, 10]
        private_check = pandair_application.PrivateAircraft(*arguments)
        assert isinstance(private_check, pandair_application.PrivateAircraft), 'Did not create PrivateAircraft'

    def test_commercial_aircraft_creation(self):

        details = ['Airbus', 300, 400, 200, 'C000', 20, 500]
        commercial_check = pandair_application.CommercialAircraft(*details)
        assert isinstance(commercial_check, pandair_application.CommercialAircraft), 'Did not create CommercialAircraft'

    def test_cargo_aircraft_creation(self):

        data = ['Bombardier', 200, 300, 250, 'CA00', 300, 20]
        cargo_check = pandair_application.CargoAircraft(*data)
        assert isinstance(cargo_check, pandair_application.CargoAircraft), 'Did not create CargoAircraft'


class AircraftMethods(unittest.TestCase):

    def test_due_for_maintenance_method_returns_true_over_30(self):
        check = ['Boeing', 100, 200, 400, 'CH00', 40]
        maintenance_check = pandair_application.Aircraft(*check).due_for_maintenance()
        self.assertTrue(maintenance_check), 'Due for maintenance not returning True over 30'

    def test_due_for_maintenance_method_returns_false_under_30(self):
        check_2 = ['Boeing', 100, 200, 400, 'CH10', 10]
        maintenance_check_2 = pandair_application.Aircraft(*check_2).due_for_maintenance()
        self.assertFalse(maintenance_check_2), 'Due for maintenance not returning False under 30'

    def test_quick_maintenance_method_cargo_set_to_zero_if_negative(self):
        check_3 = ['Boeing', 100, 200, 400, 'CA30', 100, 5]
        maintenance_aircraft = pandair_application.CargoAircraft(*check_3)
        maintenance_aircraft.quick_maintenance()
        self.assertEqual(0, maintenance_aircraft.number_flights_maintenance), 'Quick Maintenance Cargo not resetting to 0'

    def test_quick_maintenance_method_private_decreases_by_10_if_positive(self):
        check_4 = ['Boeing', 100, 200, 400, 'PR100', 100, 15]
        main_aircraft = pandair_application.PrivateAircraft(*check_4)
        main_aircraft.quick_maintenance()
        self.assertEqual(5, main_aircraft.number_flights_maintenance), 'Quick Maintenance Private not decreasing by 10'


class AirportChecks(unittest.TestCase):

    def test_airport_is_created_as_list(self):
        airport = pandair_application.Airport()
        assert isinstance(airport.airport_list, list), 'The airport created is not a list'

    def test_airport_len_method_returns_0_for_empty_airport(self):
        airport = pandair_application.Airport()
        self.assertEqual(0, len(airport)), 'Len function not returning 0 for empty airport'

    def test_add_aircraft_to_airport_method(self):
        check = ['Boeing', 100, 200, 400, 'PR100', 100, 15]
        aircraft = pandair_application.PrivateAircraft(*check)
        airport_2 = pandair_application.Airport()
        airport_2.add_aircraft(aircraft)
        self.assertEqual(1, len(airport_2)), 'Aircraft not added to Airport'

    def test_add_aircraft_that_already_exists_to_airport(self):
        check = ['Bombardier', 200, 300, 250, 'CA90', 300, 20]
        aircraft = pandair_application.CargoAircraft(*check)
        airport = pandair_application.Airport()
        airport.add_aircraft(aircraft)
        airport.add_aircraft(aircraft)
        self.assertEqual(1, len(airport)), 'Aircraft was added twice to Airport'

    def test_remove_aircraft_from_airport_method(self):
        check_1 = ['Boeing', 100, 200, 400, 'PR100', 100, 15]
        aircraft_1 = pandair_application.PrivateAircraft(*check_1)
        airport_3 = pandair_application.Airport()
        airport_3.add_aircraft(aircraft_1)
        airport_3.remove_aircraft(aircraft_1)
        self.assertEqual(0, len(airport_3)), 'Aircraft not removed from Airport'

    def test_remove_aircraft_that_does_not_exist_at_airport(self):
        check_3 = ['Boeing', 100, 200, 400, 'PR900', 100, 15]
        check_4 = ['Bombardier', 200, 300, 250, 'CA10', 300, 20]
        aircraft_3 = pandair_application.PrivateAircraft(*check_3)
        aircraft_4 = pandair_application.CargoAircraft(*check_4)
        airport_3 = pandair_application.Airport()
        airport_3.add_aircraft(aircraft_4)
        airport_3.remove_aircraft(aircraft_3)
        self.assertEqual(1, len(airport_3)), 'Aircraft not found at Airport was removed'

