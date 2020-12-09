import unittest
from ClassesInheritance import General_Patient, Diabetic_Patient
from datetime import date, timedelta

class test_Diabetic_Patient(unittest.TestCase):
    
    def test_Diabetic_Patient_object_attributes_initialization(self):
        
        first_name = 'Agnes'
        last_name = 'Janos'
        cnp = '2860515324795'
        admission_date = (2020,10,25)
        insurance = True
        medication = ['sulfonylureas', 'metformin']
        
        test_diabetic_patient = Diabetic_Patient(first_name, last_name, cnp, admission_date, insurance, medication)
        
        assert hasattr(test_diabetic_patient, 'first_name'), 'The attribute first_name is missing'
        assert hasattr(test_diabetic_patient, 'last_name'), 'The attribute last_name is missing'
        assert hasattr(test_diabetic_patient, 'cnp'), 'The attribute cnp is missing'
        assert hasattr(test_diabetic_patient, 'admission_date'), 'The attribute admission_date is missing'
        assert hasattr(test_diabetic_patient, 'insurance'), 'The attribute insurance is missing'
        assert hasattr(test_diabetic_patient, 'medication'), 'The attribute medication is missing'
        
    def test_is_at_risk_returns_correct_boolean(self):
        
        test_diabetic_patient1 = Diabetic_Patient('Agnes', 'Janos', '2860515324795', (2020,10,25), True, ['sulfonylureas', 'metformin'])
        test_diabetic_patient2 = Diabetic_Patient('Joszef', 'Janos', '1600515324795', (2020,10,25), True, ['sulfonylureas', 'metformin'])
        
        assert test_diabetic_patient1.is_at_risk() == False, 'is_at_risk_function does not return the correct boolean'
        assert test_diabetic_patient2.is_at_risk() == True, 'is_at_risk_function does not return the correct boolean'

    def test_special_placement_returns_correct_boolean(self):
        
        test_diabetic_patient1 = Diabetic_Patient('Gabriela', 'Foisoreanu', 2500929147578, (2020,10,24), True, ['metformin', 'insulin'])
        test_diabetic_patient2 = Diabetic_Patient('Mirel', 'Foisoreanu', 1680113175178, (2020,10,24), True, ['metformin'])
        
        assert test_diabetic_patient1.special_placement() == True, 'special_placement function does not return the correct boolean'
        assert test_diabetic_patient2.special_placement() == False, 'special_placement function does not return the correct boolean'

class test_General_Patient(unittest.TestCase):
    
    def test_is_dischargeable_returns_correct_boolean(self):
        
        date_three_days_ago = date.today() - timedelta(days = 3)
        date_one_day_ago = date.today() - timedelta(days = 1)
        test_general_patient1 = General_Patient('Adam', 'Vacarescu', 1621111412412, (date_three_days_ago.year, date_three_days_ago.month, date_three_days_ago.day), False)
        test_general_patient2 = General_Patient('Gabriela', 'Foisoreanu', 2500929147578, (date_one_day_ago.year, date_one_day_ago.month, date_one_day_ago.day), True)
        
        assert test_general_patient1.is_dischargeable(3) == True, 'is_dischargeable does not return correct boolean'
        assert test_general_patient2.is_dischargeable(3) == False, 'is_dischargeable does not return correct boolean'
    
    def test_payment_status_returns_correct_debt(self):
        
        test_general_patient1 = General_Patient('Adam', 'Vacarescu', 1621111412412, (2020,10,24), False)
        test_general_patient2 = General_Patient('Gabriela', 'Foisoreanu', 2500929147578, (2020,10,24), True)
        
        assert test_general_patient1.payment_status(30, 3)[2] == 90, 'payment_status function does not return correct debt'        
        assert test_general_patient2.payment_status(30, 3)[2] == 0, 'payment_status function does not return correct debt' 

if __name__ == '__main__':
    unittest.main()
        