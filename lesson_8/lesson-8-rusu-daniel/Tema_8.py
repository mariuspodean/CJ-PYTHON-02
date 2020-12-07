class Vehicle(object):
    
    def __init__(self,model,transmission,weight,cubic_capacity,number_of_seats,consumtion):
        self.transmission = transmission
        self.weight = weight
        self.cubic_capacity = cubic_capacity
        self.number_of_seats = number_of_seats
        self.consumtion = consumtion
        self.model = model
        
    def is_vehicle(self, print_result=False):
        if not print_result:
            return self.number_of_seats > 0 and self.number_of_seats < 9 and self.weight > 1000 and self.cubic_capacity > 1.0 and self.transmission == 'Automatic' or self.transmission == 'Manual' or self.transmission =='Semi-Automatic'
        # cum pot sa fac aici sa returneze number_of_seats doar pentru numere intregi mai mari ca 0
    @staticmethod
    def message():
        return f'This is my favorite vehicle'
      
class Sport_Car(Vehicle):
    
    def __init__(self,model,transmission,weight,cubic_capacity,number_of_seats,consumtion,acceleration,horse_power,top_speed,torque,price):
        super(Sport_Car, self).__init__(model,transmission,weight,cubic_capacity,number_of_seats,consumtion)
        self.acceleration = acceleration
        self.horse_power = horse_power
        self.price = price
        self.top_speed= top_speed
        self.torque = torque
        self.price = price
        
        
    def is_sport_car(self,sport_car=False):
        if not sport_car:
            return self.cubic_capacity > 3 and self.acceleration > 4 and self.horse_power > 250 and self.top_speed > 210 and torque > 300 and self.consumtion > 17
    
    def __repr__(self):
        return f'''The specs are: {self.model} has the specs transmission {self.transmission}, weight {self.weight},
a cubic capacity of {self.cubic_capacity}liters, {self.number_of_seats} seats, a consumtion of {self.consumtion} 10l/100km, acceleration from 0-100km/h {self.acceleration}seconds,
hp {self.horse_power}, top speed of {self.top_speed},torque {self.torque}Lb-Ft, and a price of {self.price} euros '''
           
               
# car =(model,transmission,weight,cubic_capacity,number_of_seats,consumtion,acceleration,horse_power,top_speed,torque,price)
audi= Sport_Car('S3','Automatic',1500,2.0,4,17,4.8,273,212, 320, 45000)         
bmw=Sport_Car('M5','Automatic',1700,3.0,4,20,4.1,310,220,350,70000)
VW=Sport_Car('Golf','Manual',1270,1.9,5,8,6,170,180,234,20000)
Renault=Sport_Car('Megane','Dual-clutch',1400,1.6,5,8,7.8,105,180,200,12000)
Toyota=Sport_Car('Supra','Semi-Automatic',1550,3.0,2,19,3.4,385,230,364,63000)

print(audi.is_vehicle())
print(audi.is_sport_car())
print(audi)
print(audi.message())

print(bmw.is_vehicle())
print(bmw.is_sport_car())
print(bmw)
print(bmw.message())

print(VW.is_vehicle())
print(VW.is_sport_car())
print(VW)
print(VW.message())

print(Renault.is_vehicle())
print(Renault.is_sport_car())
print(Renault)
print(Renault.message())

print(Toyota.is_vehicle())
print(Toyota.is_sport_car())
print(Toyota)
print(Toyota.message())



