import sys
import unittest
from final_project.implementation import Person
from final_project.implementation import Kindergarten
from final_project.implementation import Kid
from final_project.implementation import Group

class TestPerson(unittest.TestCase):

   def test_person_object_attribute_initialization(self):

        test_person = Person('Person', 'M', '12-12-2001', '0750336679')

        assert hasattr(test_person, '_name'), 'Person class is missing _name attribute'
        assert hasattr(test_person, '_gender'), 'Person class is missing _gender attribute'
        assert hasattr(test_person, '_date_of_birth'), 'Person class is missing _date_of_birth attribute'
        assert hasattr(test_person, '_phone_number'), 'Person class is missing _phone_number attribute'

   def test_person_object_attribute_values(self):

        name = 'Person'
        gender = 'M'
        date_of_birth = '12-12-2001'
        phone_number = '0750336679'
        test_person = Person(name, gender, date_of_birth, phone_number)

        self.assertEqual(test_person._name, name), 'Person class _name attribute value is wrong'
        self.assertEqual(test_person._gender, gender), 'Person class _gender attribute value is wrong'
        self.assertEqual(test_person._date_of_birth, date_of_birth), 'Person class _date_of_birth attribute value is wrong'
        self.assertEqual(test_person._phone_number, phone_number), 'Person class _phone_number attribute value is wrong'

   def test_person_object_age(self):

        p1, p2, p3 = Person('Person1', 'M', '10-02-2015', '0729315687'), Person('Person2', 'F', '10-02-2015', '0759335565'), Person('Person3', 'F', '10-02-2017', '0757835565')

        age1 = p1.get_age()
        age2 = p2.get_age()
        age3 = p3.get_age()

        self.assertEqual(age1, age2), 'Person1 and Person2 age not equal'
        self.assertNotEqual(age1, age3), 'Person1 and Person3 age are equal'



class TestKindergarten(unittest.TestCase):

     def test_register_kid(self):

          kindergarten = Kindergarten ('Kitty')
          self.assertIsInstance (kindergarten, Kindergarten), 'Invalid Kindergarten instance'

          kid = Kid('Siriciuc Anisia', 'F', '06-07-2018', '0755955363', 'Siriciuc Alexandra')
          self.assertIsInstance (kid, Kid), 'Invalid Kid instance'

          kindergarten.register_kid(kid)
          group = kindergarten.get_group_by_name(Kindergarten.baby_group_name)
          self.assertIsInstance (group, Group), 'INvalid Group instance'

          self.assertEqual((len(group.get_kids_list())), 1),'Kid was not registred'

          baby_kid = group.get_kids_list()[0] 
          self.assertIs (kid, baby_kid), 'Wrong kid registration'

          
          
if __name__ == '__main__':
    unittest.main()
