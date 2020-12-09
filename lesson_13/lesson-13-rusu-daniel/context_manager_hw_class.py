sheet_population = [
('Berlin',3748148),
('Hamburg',1822445),
('Munich',1471508),
('Cologne',1085664),
('Frankfurt',753056),
]

my_dict = { country:population for country,population in sheet_population }

class JustSomeExceptions():
    def __enter__(self):
        self.my_dict = my_dict
        self.sheet_population=sheet_population
        return "Indicator"
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is KeyError:
            print('!!!ERROR!!! This key do not exists')
            return True
        if exc_type is IndexError:
            print('!!!ERROR!!! Out of range index')
            return True

#test1 Success            
with JustSomeExceptions() as tester:
       key='Berlin'
       if key in my_dict.keys():
           key_has_value=my_dict['Berlin']
           print(f'The searched key {key} was found and has the associated value {key_has_value}')
       print(tester)

print(tester)
print('No more\n')

#test2 True
with JustSomeExceptions() as tester:
    print(range(len(sheet_population)))
    print(f'The value at the specified index is {sheet_population[0]}')
    print(tester)

print(tester)
print('No more\n')

#test1 Error
with JustSomeExceptions() as tester:
           key_has_value=my_dict['Koln']
           print(f'The searched key was found and has the associated value {key_has_value}')
           print(tester)

print(tester)
print('No more\n')

#test2 Error
with JustSomeExceptions() as tester:
    print(range(len(sheet_population)))
    print(f'The value at the specified index is {sheet_population[8]}')
    print(tester)

print(tester)
print('No more')





