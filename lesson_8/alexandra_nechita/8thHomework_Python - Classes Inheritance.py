from datetime import date

class General_Patient (object):
    
    hospital = 'Regina Maria'
    
    def __init__(self, first_name, last_name, cnp, admission_date, insurance):
        self.first_name = first_name
        self.last_name = last_name
        self.cnp = str(cnp)
        self.admission_date = admission_date
        self.insurance = insurance
        
    def is_dischargeable (self, days_of_hospitalization):
        days_in_hospital = (date.today() - date(self.admission_date[0],self.admission_date[1], self.admission_date[2])).days
        if days_in_hospital == days_of_hospitalization:
            return True
        else:
            return False
        
    def discharge_message (self, days_of_hospitalization):
        days_in_hospital = (date.today() - date(self.admission_date[0],self.admission_date[1], self.admission_date[2])).days
        if self.is_dischargeable(days_of_hospitalization):
            print (f'The patient {self.first_name} {self.last_name} is to be discharged today, {date.today()} \n')
        elif days_in_hospital < days_of_hospitalization:
            print(f'The patient {self.first_name} {self.last_name} is to be discharged {days_of_hospitalization - (date.today() - date(self.admission_date[0],self.admission_date[1], self.admission_date[2])).days} day(s) from today \n')
        else:
            print(f'The health situation of the patient {self.first_name} {self.last_name} requires extended hospitalization \n')
        
    def payment_status (self, cost_per_day, days_of_hospitalization):
        if self.insurance:
            return f'The patient {self.first_name} {self.last_name} has nothing to pay \n'
        else:
            return f'The patient {self.first_name} {self.last_name} has to pay {cost_per_day*days_of_hospitalization} ron \n'
        
    def __repr__(self):
        class_name = type(self).__name__
        return "Dev view: "'{}. Name: {} {}; CNP: {}; ID: {}; \n'.format(class_name, self.first_name, self.last_name, self.cnp, id(self))
        
    def __str__(self):
        if self.insurance:
            return f'This is the patient {self.first_name} {self.last_name}, with the CNP {self.cnp}. The patient has insurance. \n'
        else:
            return f'This is the patient {self.first_name} {self.last_name}, with the CNP {self.cnp}. The patient has no insurance. \n'
    
    @staticmethod
    def hospital_motto():
        return 'Good is not enough \n'

class Diabetic_Patient (General_Patient):
    
    def __init__(self, first_name, last_name, cnp, admission_date, insurance, medication):
        self.medication = medication
        super().__init__(first_name, last_name, cnp, admission_date, insurance)
    
    def is_at_risk (self):
        current_date = date.today()
        gendre_number = int(self.cnp[slice(0,1)])
        year = int(self.cnp[slice(1,3)])
        motnh = int(self.cnp[slice(3,5)])
        if gendre_number == 1 or gendre_number == 2:
            birth_year = 1900 + year
            if current_date.year - birth_year > 55:
                return True
        return False
    
    def risk_message(self):
        if self.is_at_risk():
            print(f'Patient {self.first_name} {self.last_name} has a higher risk of comorbidities \n')
            pass
        print(f'No extra measures are needed for patient {self.first_name} {self.last_name} \n')

    def placement (self):
        for medicine in self.medication:
            if medicine == 'insulin':
                return f'Patient {self.first_name} {self.last_name} is to be placed in a special room \n'
        return f'Patient {self.first_name} {self.last_name} can be placed in any room is available first \n'
    
patient_1 = Diabetic_Patient('Eszter', 'Pop', '2860515324795', (2020,10,25), True, ['sulfonylureas', 'metformin'])
patient_2 = Diabetic_Patient('Marin', 'Barnutiu', 1500225322791, (2020,11,28), False, [])
patient_3 = Diabetic_Patient('Adam', 'Vacarescu', 1621111412412, (2020,10, 20), False, [])
patient_4 = Diabetic_Patient('Gabriela', 'Foisoreanu', 2500929147578, (2020,10,24), True, ['metformin', 'insulin'])
patient_5 = Diabetic_Patient('Mirel', 'Foisoreanu', 1680113175178, (2020,10,24), True, ['metformin'])
    
print (General_Patient.hospital_motto())

print (patient_1.first_name, patient_1.last_name, patient_1.cnp, patient_1.admission_date, patient_1.insurance)
patient_1.discharge_message(0)
print (patient_1.payment_status(75, 3))
print (repr(patient_1))
print (str(patient_1))

print ('*' * 113)

print (patient_2.first_name, patient_2.last_name, patient_2.cnp, patient_2.admission_date, patient_2.insurance)
patient_2.discharge_message(6)
print (patient_2.payment_status(75, 3))
print (repr(patient_2))
print (str(patient_2))

print ('*' * 113)

print (patient_3.first_name, patient_3.last_name, patient_3.cnp, patient_3.admission_date, patient_3.insurance)
patient_3.discharge_message(3)
print (patient_3.payment_status(100, 5))
print (repr(patient_3))
print (str(patient_3))
print (patient_3.hospital)
        
print ('*' * 113)

print (patient_4.first_name, patient_4.last_name, patient_4.cnp, patient_4.admission_date, patient_4.insurance)
patient_4.discharge_message(3)
print (patient_4.payment_status(100, 5))
print (repr(patient_4))
print (str(patient_4))
patient_4.risk_message()
print (patient_4.placement())

print ('*' * 113)

patient_5.risk_message()
print (patient_5.placement())
        
    
        
   
        
  
        