import logging
import time
from random import randint
from contextlib import contextmanager
from random import randrange
from datetime import datetime

now = datetime.now()

# logging settings
logging.basicConfig(level=logging.DEBUG, filemode="a", filename="history.txt")


# Decorator
def log_operation(function):
    def wrapper(*args, **kwargs):
        time = now.strftime("[%Y-%m-%D %H:%M:%S]")
        logging.debug(time + "Operation performed:" + repr(function))
        for arg in args:
            logging.debug(time + "Parameter : " + repr(arg))
        return function(*args, **kwargs)

    return wrapper


# Mutable Mapping
class Bouquet:
    def __init__(self, bouquet_name=None, bouquet_flowers=None):
        self.bouquet_name = bouquet_name
        self.bouquet_flowers = bouquet_flowers

    # String and representation implemented
    def __repr__(self):
        print_string = f'{self.bouquet_name}: {self.bouquet_flowers}'
        return print_string

    def __str__(self):
        print_string = ''
        bouquet_title = f'{self.bouquet_name}\n'
        print_string = ''.join((print_string, bouquet_title))
        return print_string

    # Operator overloading
    # Decorators usage
    @log_operation
    def __add__(self, other):
        bouquet_name = self.bouquet_name + " and " + other.bouquet_name
        bouquet_flowers = {}
        for b1 in self.bouquet_flowers:
            bouquet_flowers[b1] = self.bouquet_flowers[b1]
        for b2 in other.bouquet_flowers:
            if bouquet_flowers.get(b2) != None:
                bouquet_flowers[b2] += other.bouquet_flowers[b2]
            else:
                bouquet_flowers[b2] = other.bouquet_flowers[b2]

        return Bouquet(bouquet_name, bouquet_flowers)

    def __len__(self):
        return len(self.bouquet_flowers)

    def __iter__(self):
        return self.bouquet_flowers

    def __getitem__(self, item):
        return self.bouquet_flowers[item]

    def __contains__(self, item):
        return item in self.bouquet_flowers

    def keys(self):
        return self.bouquet_flowers.keys()

    def values(self):
        return self.bouquet_flowers.values()

    def items(self):
        return self.bouquet_flowers.items()


# Sequence
class BouquetBox:
    def __init__(self, stock):
        self._bouquetBox_list = stock

    # String and representation implemented
    def __repr__(self):
        representation = '['
        for bouquet in self._bouquetBox_list:
            representation += '{' + f'{bouquet.bouquet_name}:{bouquet.bouquet_flowers}' + '}'
        representation += ']'
        return representation

    def __str__(self):
        print_string = ''
        for bouquet in self._bouquetBox_list:
            bouquet_title = f'{bouquet.bouquet_name}\n'
            print_string = ''.join((print_string, bouquet_title))
        return print_string

    def __len__(self):
        return len(self._bouquetBox_list)

    def __getitem__(self, index):
        return self._bouquetBox_list[index]

    def __contains__(self, item):
        return item in self._bouquetBox_list

    def __setitem__(self, index, value):
        self._bouquetBox_list[index] = value

    def __delitem__(self, index):
        del self._bouquetBox_list[index]

    def remove(self, item):
        self._bouquetBox_list.remove(item)

    def append(self, item):
        self._bouquetBox_list.append(item)

    # eliminate a bouquet from bouquetBox list by its index
    def pop(self, index=None):
        if index:
            return self._bouquetBox_list.pop(index)
        else:
            return self._bouquetBox_list.pop()

    # method get a bouquet as argument, extract the bouquet from bouquetBox and print it
    def pick(self, bouquet=None):
        if bouquet:
            index = self._bouquetBox_list.index(bouquet)
        else:
            max_rand_no = len(self._bouquetBox_list)
            index = randrange(0, max_rand_no, 1)

        return self._bouquetBox_list[index]


class PrettyPrinter():
    def __init__(self, name=None, flowers=None):
        self.name = name
        self.flowers = flowers

        super().__init__(name, flowers)

    def pretty_print(self):
        header = ''' 
_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._
 ,'_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._`.'''
        footer = '''
( (_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._) )
 `._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._,'''
        spacer = '''
 ) )                                                       ( ('''
        to_print = header
        print('++++++++++++++++++')
        if (self.name):
            to_print += self.__replace_line__(self.name) + spacer
        else:
            to_print += self.__replace_line__('Our Stock') + spacer
        for flower in self.flowers.items():
            (key, value) = flower
            replace_with = key + ' : ' + str(value)
            to_print += self.__replace_line__(replace_with) + spacer
        to_print += footer
        print(to_print)

    def __replace_line__(self, replace_with):
        filler = '''
( (                                                         ) )'''
        to_replace = len(replace_with) * ' '
        return filler.replace(to_replace, replace_with, 1)


# Inheritance + Mixin
class PrettyBouquet(PrettyPrinter, Bouquet):
    pass


# Context Manager + Generator
class BouquetManager():
    def __init__(self):
        print('Welcome to the Bouquet store')

    def __enter__(self):
        print('I am the Bouquet Manager.')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Thank you for comming!')
        print('Goodbye!')


def enter_store(stock):
    with BouquetManager() as manager:
        val = 'h'
        items_bought = []
        while val != 'q':
            val = input("""How can I help you:
            l - list stock
            b - buy bouquet
            m - merge all purchases
            p - print purchases
            q - good bye
            """)
            if val == 'l':
                print(str(stock))
            elif val == 'b':
                item = input(f'Buying item [0 to {len(stock)-1}]:')
                items_bought.append(stock[int(item)])
                yield stock[int(item)]
            elif val == 'p':
                print("Printing purchased items:")
                for item in items_bought:
                    print("----------")
                    pretty_bouquet = PrettyBouquet(item.bouquet_name,
                                                   item.bouquet_flowers)
                    pretty_bouquet.pretty_print()
            elif val == 'm':
                print('Merging all purchased items:')
                if len(items_bought) > 0:
                    sum = items_bought[0]
                    for item in items_bought[1:]:
                        # operator overloading of +
                        sum = sum + item
                items_bought = [sum]
                print(items_bought)
        return items_bought
