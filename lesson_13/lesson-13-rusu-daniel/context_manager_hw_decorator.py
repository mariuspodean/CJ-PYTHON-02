#Implement a context manager called just_some_exceptions that will handle KeyError, IndexError by printing a message and let any other exceptions propagate outside of the context manager.

#Implement the context manager by using both approaches: by using class and by using @contextmanager

#Write examples that prove the functionality for all the handled exceptions and for one exception that is not handled.

from contextlib import contextmanager

sheet_population = [
('Berlin',3748148),
('Hamburg',1822445),
('Munich',1471508),
('Cologne',1085664),
('Frankfurt',753056),
]

my_dict = { country:population for country,population in sheet_population }

@contextmanager
def just_some_exceptions(x):
   error_message=''
   try:
       yield 'Reached yield'
   except KeyError:
       error_message = '!!!ERROR!!! This key is not in the dictionary!'
   except IndexError:
       error_message = '!!!ERROR!!! This index is out of the limit!'
   finally:
        if error_message:
           print(error_message)
        else:
           print('No exception appeard')

#test1 Success
with just_some_exceptions(my_dict) as tester:
       key='Berlin'
       if key in my_dict.keys():
           key_has_value=my_dict['Berlin']
           print(f'The searched key {key} was found and has the associated value {key_has_value}')
       print(tester)

print(tester)
print('No more\n')

#test2 Success
with just_some_exceptions(sheet_population) as tester:
    print(range(len(sheet_population)))
    print(f'The value at the specified index is {sheet_population[0]}')
    print(tester)

print(tester)
print('No more\n')

#test1 Error
with just_some_exceptions(my_dict) as tester:
           key_has_value=my_dict['Koln']
           print(f'The searched key was found and has the associated value {key_has_value}')
           print(tester)

print(tester)
print('No more\n')

#test2 Error
with just_some_exceptions(sheet_population) as tester:
    print(range(len(sheet_population)))
    print(f'The value at the specified index is {sheet_population[8]}')
    print(tester)

print(tester)
print('No more')


