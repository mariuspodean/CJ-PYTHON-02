from datetime import datetime
from datetime import date 
import logging


logging.basicConfig(level=logging.DEBUG, filename = 'kindergarten_log')

log = logging.getLogger(__name__)


class Person:

    def __init__(self, name, gender, date_of_birth, phone_number):
        self._name = name
        self._gender = gender
        self._date_of_birth = date_of_birth
        self._phone_number = phone_number
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
    
    def get_gender(self):
        return self._gender
    
    def set_gender(self, gender):
        self._gender= gender

    def get_date_of_birth(self):
        return self._date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth
    
    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def get_age(self):
        log.info(' get age method')
        try:
            birth_date = datetime.strptime(self._date_of_birth, '%d-%m-%Y')
            today = date.today() 
            year = today.year - birth_date.year
            months= today.month - birth_date.month
        except ValueError as e:
            log.warning(f'Invalid date of birth: {e.__str__()}')
        else:
            log.debug(f' Kid {self.get_name()} has {year} years and {months} months')
            return (year, months)
    
    def __str__(self):
        return f' {self.__class__.__name__}: {self._name}, {self._gender}, {self._date_of_birth}, {self._phone_number}'

    def __repr__(self):
        return f' {self.__class__.__name__} ({self._name}, {self._gender}, {self._date_of_birth}, {self._phone_number}) with id: {id(self)}'   



class Kid(Person):

    def __init__(self, name, gender, date_of_birth, phone_number, parent_name):
        super().__init__(name, gender, date_of_birth, phone_number)
        self._parent_name = parent_name

    def get_parent_name(self):
        return self._parent_name
    
    def set_parent_name(self, parent_name):
        self._parent_name = parent_name

    def __gt__(self, other):
        log.info (' greater method')
        year, month = self.get_age()
        other_year, other_month = other.get_age() 
        if year > other_year:
            log.debug (f' Kid {super().get_name()} is greater than Kid {other.get_name()}')
            return True
        elif year < other_year:
            log.debug (f' Kid {other.get_name()} is greater than Kid {super().get_name()}')
            return False
        elif month > other_month:
            log.debug (f' Kid {super().get_name()} is greater than Kid {other.get_name()}')
            return True
        else:
            log.debug (f' Kid {other.get_name()} is greater than Kid {super().get_name()}')
            return False 
            
    def __str__(self):
        return f'{self.__class__.__name__} :  {self._name}, {self._gender}, {self._date_of_birth}, {self._phone_number}, {self._parent_name}'

    def __repr__(self):
        return f'{self.__class__.__name__} ({self._name}, {self._gender}, {self._date_of_birth}, {self._phone_number}, {self._parent_name}) with id: {id(self)}'


class Teacher(Person):

    def __init__(self, name, sex, date_of_birth, phone_number, salary):
        super().__init__(name, sex, date_of_birth, phone_number)
        self._salary = salary

    def get_salary(self):
        return self._salary
    
    def set_salary(self, salary):
        self._salary = salary
    
    def get_annual_salary(self, salary):
        annual_salary = self._salary * 12
        return annual_salary

    def __str__(self):
        return f'{self.__class__.__name__}: {self._name}, {self._gender}, {self._date_of_birth}, {self._phone_number}, {self._salary}'

    def __repr__(self):
        return f'{self.__class__.__name__} ({self._name}, {self._gender}, {self._date_of_birth}, {self._phone_number}, {self._salary}) with id: {id(self)}'



class Group:

    def __init__(self, name, teacher, iterable= []):
        self._name = name
        self._teacher = teacher
        self._kids_list = list(iterable)

    def get_name(self):
        return self._name

    def get_teacher(self):
        return self._teacher
    
    def set_teacher (self, teacher):
        self._teacher = teacher
        
    def __getitem__ (self, index):
        return self._kids_list[index]

    def __setitem__(self, index, kid):
        self._kids_list[index] = kid

    def __delitem__(self, index):
        return self._kids_list.pop(index)

    def __len__ (self):
        return len (self._kids_list)

    def add_kid(self, kid):
        self._kids_list.append(kid)

    def remove_kid(self, kid):
        self._kids_list.remove(kid)

    def get_kids_list(self):
        return self._kids_list

    def __str__(self):
        return f'{self.__class__.__name__} {self._name} : {self._teacher}, {self._kids_list}'
        
    def __repr__(self):
        return f'{self.__class__.__name__} {self._name} : {self._teacher}, {self._kids_list} with id :{id(self)}'



class FileHandler:

    def __init__(self, file_name, file_mode):
        self._file_name = file_name
        self._file_mode = file_mode
        self._file_handle = None
    
    def __enter__(self):
        self._file_handle = open(self._file_name, self._file_mode)
        log.debug (f' The file {self._file_name} is created')
        return self._file_handle

    def __exit__(self, exc_type,exc_value, exc_traceback):
        self._file_handle.close()


   
class Menu:

    def __init__(self, start_date, price, iterable):
        self._dict = dict(iterable)
        self._start_date = start_date
        self._price = price

    def get_start_date(self):
        return self._start_date

    def set_start_date(self, start_date):
        self._start_date = start_date

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def print_file(self):
        with FileHandler('menu.txt', 'w') as menu_file:
            menu_file.write('Menu start date: ' + str(self._start_date) + '\n')
            menu_file.write('Menu price: ' + str(self._price) + ' EUR' + '\n\n')
            for k, v in self._dict.items():
                menu_file.write(str(k) + ':' + '\n')
                for subkey, subvalue in v.items():
                    menu_file.write('   ' + str(subkey) + ': ' + ', '.join([str(element) for element in subvalue]) + '\n')
                menu_file.write('\n')

    def get_menu(self):
        return self._dict

    def __getitem__(self, key):
        return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __delitem__(self, key):
        del self._dict[key]

    def __contains__(self, key):
        return key in self._dict

    def __len__(self):
        return len(self._dict)

    def __str__(self):
        return f' {self.__class__.__name__}, {self._dict}'

    def __repr__(self):
        return f' {self.__class__.__name__}, {self._dict} with id: {id(self)}'


def menu_daily_generator(my_menu):
    log.debug (' Generate the menu for the days of the weeks:')
    for k, v in my_menu.get_menu().items():
        yield k, v


list_menu_archive = []
def archive_menu_list (func):
    def wraper(self=None, menu=None):
        list_menu_archive.append(func(self, menu))
        log.debug ('Create the list menu archive')
    return wraper


class Kindergarten:

    baby_group_name = 'Babies'
    first_group_name = 'Bees'
    second_group_name = 'Toddlers'
    third_group_name = 'Heros'

    default_groups = {baby_group_name: (1.5, 3), first_group_name: (3,4), second_group_name:(4,5), third_group_name: (5,6)}

    def __init__(self, name):
        self._name = name
        self._teacher_list = []
        self._group_dict = {}
        self._menu_list = []

    def get_name(self):
        return self._name

    def add_group(self, group):
        self._group_dict[group.get_name()] = group
    
    def remove_group(self, group):
        if group.get_name() in self._group_dict:
            self._group_dict.pop(group.get_name())

    def get_group_by_name (self, group_name):
        if group_name in self._group_dict:
            return self._group_dict[group_name]
        return None

    def add_teacher(self, teacher):
        self._teacher_list.append(teacher)

    def remove_teacher(self, teacher):
       for teacher_item in self._teacher_list:
           if teacher_item.get_name() == teacher.get_name():
               self._teacher_list.remove(teacher)

    def add_menu(self, menu):
        self._menu_list.append(menu)

    @archive_menu_list
    def remove_menu(self, menu):
        self._menu_list.remove(menu)
        return menu

    def find_teacher(self, teacher):
        for teacher_item in self._teacher_list:
            if teacher_item == teacher:
                return True
        return False

    def get_kid_group(self, kid):
        year, month = kid.get_age()
        month
        for group_name, (min_age, max_age) in self.default_groups.items():
            if year >= min_age and year < max_age:
                if group_name in self._group_dict:
                    group = self._group_dict[group_name]
                    return group
        return None

    def find_kid(self, kid):
        group = self.get_kid_group(kid)
        if None != group:
            for kid_item in group.get_kids_list():
                if kid.get_name() == kid_item.get_name():
                    return True
            return False
        else:
            return False

    def register_kid (self, kid):
        log.info ('register kid method')
        group = self.get_kid_group(kid)
        if None != group:
            group.add_kid(kid) 
            log.debug(f' Kid {kid.get_name()} registred in group {group.get_name()}')
        else:
            log.debug(f' Kid: {kid.get_name()} not matched any group')
            

    def unregister_kid(self, kid):
        log.info ('unregister kid method')
        group = self.get_kid_group(kid)
        if None != group:
            group.remove_kid(kid) 
            log.debug(f' Kid {kid.get_name()} unregistred from group {group.get_name()}')
        else:
            log.debug(f' Kid: {kid.get_name()} not found in any group')


    def __str__(self):
        return f'{self.__class__.__name__} {self._name}'
        
    def __repr__(self):
        return f'{self.__class__.__name__} {self._name}  with id :{id(self)}'



class PrettyPrinter:
    def pretty_printer(group):
        print("*" * 50)
        print (f'                Group name:', group.get_name())
        print(f'                                  Teacher name:', group.get_teacher().get_name())
        print("*" * 50)
        for index, kid in enumerate (group.get_kids_list(), start = 1):
            print(f'{index}{"."} {kid.get_name()}')
            
        print("*" * 50)

class PrintGroup (Group, PrettyPrinter):
    pass
