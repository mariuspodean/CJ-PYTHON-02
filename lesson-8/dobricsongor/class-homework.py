class AllCar:
    
    def __init__(self,company,type,color,speed,value):
        self.company = company
        self.type = type
        self.color = color
        self.speed = speed
        self.value = value

    def __str__(self):
        return f'The {self.color} {self.company} {self.type}\'s speed is {self.speed} km/h and worth {self.value} EUR.'

    def __repr__(self):
        return f'{self.company} {self.type}: {self.color}, [{self.speed},{self.value}]'

    def is_fast(self):
        return self.speed >= 100



class RacingCar(AllCar):

    def __init__(self,company,type,color,speed,value,horsepower):
        self.horsepower = horsepower
        super().__init__(company,type,color,speed,value)

    
    def __str__(self):
        return f'The {self.color} {self.company} {self.type}\'s speed is {self.speed} km/h and has {self.horsepower} HP.'


    def is_fast(self):
        return f'Is this a fast car? {self.speed >= 200}'

    
    @staticmethod
    def welcome_message():
        return ('''*********Welcome to the competition 2020! *******
        *******You're allowed to race!******
        *******The race is about to start.*******
        *******Start your engines! 3..2..1.. GO!*******''')
           
    
    def is_allowed_to_race(self):
        print ('Is this car allowed to race? ') 
        if self.is_fast and self.horsepower > 400:
            return RacingCar.welcome_message()
        else:
            return False


    def discount_if_expensive(self):
        message = f'This car worth {self.value} EUR.'
        if self.value > 50000:
            return f'{message}...but you can have it with an extra 10% discount: {int((self.value)-(self.value/10))} EUR'
        else:
            return message

    @classmethod
    def from_dict(cls, dictionary):
        company = dictionary['company']
        type = dictionary['type']
        color = dictionary['color']
        speed = dictionary['speed']
        value = dictionary['value']
        horsepower = dictionary['horsepower']
        
        return cls(company,type,color,speed,value,horsepower)


car1 = RacingCar('Volkswagen','Passat','silver',140, 12000, 140)
car2 = RacingCar('Ford','Mustang','black', 220, 40000, 350)
car3 = RacingCar('Ferrari','F400','red',350, 300000, 700)

more_cars = RacingCar.from_dict(
    {'company': 'Dodge', 'type' : 'Charger', 'color': 'yellow', 'speed': 250, 'value': 70000, 'horsepower': 500}
)


print(str(car1))
print(car1.discount_if_expensive())
print(car1.is_fast())
print(car1.is_allowed_to_race())
print('*'*50)

print(str(car2))
print(car2.discount_if_expensive())
print(car2.is_fast())
print(car2.is_allowed_to_race())
print('*'*50)

print(str(car3))
print(car3.discount_if_expensive())
print(car3.is_fast())
print(car3.is_allowed_to_race())
print('*'*50)


print(str(more_cars))
print(more_cars.discount_if_expensive())
print(more_cars.is_fast())
print(more_cars.is_allowed_to_race())

