import logging
import time
from random import randint
from contextlib import contextmanager
from random import randrange


procurement_list_archive=[]

class Bouquet:

    def __init__(self, bouquet_name=None, bouquet_flowers=None):
        self.bouquet_name = bouquet_name
        self.bouquet_flowers = bouquet_flowers

    def __repr__(self):
        print_string = f'{self.bouquet_name}: {self.bouquet_flowers}'
        return print_string

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


class BouquetBox:

    def __init__(self):
        self._bouquetBox_list = []

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

class Stock:
    
    def __init__(self,name=None, inside_stock=None):
        self.inside_stock = inside_stock
        self.name = name
       
# When printing the stock object, it will print similar to a bouquet, its content.
    def __str__(self):
        print_content = ''
        for flower in self.inside_stock:
            print_content = ' '.join((print_content, flower, str(self.inside_stock[flower]))) 
            print_content = f'{print_content}\n'
        return print_content



# def __repr__(self):
#         print_content = ''
#         for flower in self.inside_stock:
#             print_content = ' '.join((print_content, flower, str(self.inside_stock[flower]))) 
#             print_content = f'{print_content}\n'
#         return print_content




#  mutable mapping
    def __contains__(self, flower):
        return flower in self.inside_stock

# We can also ask if a certain product is in stock
    def check_flower(self, flower):
        if flower in self.inside_stock:
            print ('Flower in stock')
    
    def __iter__(self):
        return iter(self.inside_stock)

    def __len__(self):
        return len(self.inside_stock)

    def __getitem__(self, flower):
        return self.inside_stock[flower]

    def __setitem__(self, flower, quantity):
        self.inside_stock[flower] = quantity

    def __delitem__(self, flower):
        del self.inside_stock[flower]

# We can add new items in the stock.
    def add_flower_in_stock(self, flower, quantity):
        if flower in self.inside_stock:
            self.inside_stock[flower] += quantity
        else:
            self.inside_stock[flower] = quantity

# We can [...] remove existing ones. Tot aici actualizam cantitatile in minus. Anuntam cand ramanem fara ceva in stock
    def remove_flower_from_stock(self, flower, quantity):
        if flower in self.inside_stock:
            self.inside_stock[flower] = self.inside_stock[flower] - quantity
            if self.inside_stock[flower] <= 0:
                print (f'No more {flower} in stock.')
                del self.inside_stock[flower]
        else:
            print ('No such flower in stock')
    
    def check_bouquet(self,bouquet)->[]:
        list_we_have = []
        list_to_shop = []
        for flower in bouquet.keys():
            if flower in self:
                if self[flower] >= bouquet[flower]:
                    list_we_have.append(flower)
                else:
                    quantity_to_buy = bouquet[flower] - self[flower]
                    list_to_shop.append((flower, quantity_to_buy))
            else:
                list_to_shop.append((flower,bouquet[flower]))
        print (f'We already have: {list_we_have}')
        print (f'We need to buy: {list_to_shop}')
        return list_to_shop

    def update(self,flower):
        if(self.inside_stock is None):
            self.inside_stock = {}
        for flower in flower.items():
            (name,quantity)= flower
            self.inside_stock[name]= quantity
    
    def update_quantity(self, flower,quantity):
        pass
                

class PrettyPrinter():

    def __init__(self,name=None,flowers=None):
        self.name = name
        self.flowers = flowers
        
        super().__init__(name,flowers)
    
    def pretty_print(self):
        header = ''' 
_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._
 ,'_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._`.'''
        footer = '''
( (_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._) )
 `._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._,'''
        spacer = '''
 ) )                                                       ( ('''
        to_print=header
        if(self.name):
            to_print+= self.__replace_line__(self.name) + spacer
        else:
            to_print+= self.__replace_line__('Our Stock') + spacer
        for flower in self.flowers.items():
            (key,value) = flower
            replace_with = key + ' : '+ str(value)
            to_print += self.__replace_line__(replace_with) + spacer
        to_print+=footer
        print(to_print)

    def __replace_line__(self,replace_with):
        filler ='''
( (                                                         ) )'''
        to_replace = len(replace_with)*' '
        return filler.replace(to_replace,replace_with,1)

class PrettyBouquet(PrettyPrinter,Bouquet):
    pass


class PrettyStock(PrettyPrinter,Stock):
    pass

def check_the_stock(stock, bouquets):
    half_or_more_flowers_bouquets = []
    less_than_half_flowers_bouquets = []
    for bouquet in bouquets:
        available_flowers = 0
        for flower in bouquets.keys():
            if flower in stock:
                available_flowers += 1
        if available_flowers >= (len(bouquet.keys())/2):
            half_or_more_flowers_bouquets.append(bouquet.bouquet_name)
        else:
            less_than_half_flowers_bouquets.append(bouquet.bouquet_name)
    print(f'We have half or more flowers for: {half_or_more_flowers_bouquets}')
    print(f'We have less than half flowers for: {less_than_half_flowers_bouquets}')
    return half_or_more_flowers_bouquets          

# check_the_stock(our_stock, our_bouquets_box)

def pretty_print_bouquet(function):

    def wrapper(stock,bouquet):
        procurement_list=function(stock,bouquet)
        missing_items = PrettyBouquet("Flowers needed",procurement_list)
        missing_items.pretty_print()
        return procurement_list

    return wrapper

def archive_procurement_list(fnc2):
    def inner_func_2(stock, bouquet):
        procurement_list = fnc2(stock, bouquet)
        time_now = time.localtime()
        date_today = time.strftime('%d %m %Y', time_now)

        if type(procurement_list) == dict:
            procuremet_list_archive.append((date_today, bouquet.bouquet_name, procurement_list))

        return procurement_list

    return inner_func_2

@archive_procurement_list
@pretty_print_bouquet
def prepare_procurement_list(stock, bouquet):
    procurement_list = {}
    for flower in bouquet.keys():
        if flower in stock:
            if stock[flower] <= bouquet[flower]:
                quantity_to_buy = bouquet[flower] - stock[flower]
                procurement_list.update({flower: quantity_to_buy})
    print (f'Procurement list: {procurement_list}')
    return procurement_list

# #OPERATOR OVERLOADING
# class LilyBouquets:

#     def __init__(self, bouquet):
#         self.bouquet = bouquet

#     def __str__(self):
#         return self.bouquet

#     def __add__(self, other):
#         return SpecialBouquet(f'{self.bouquets + other.bouquet} concatenated from {self.bouquet} and {other.bouquet}')


# class RosesBouquet:

#     def __init__(self, bouquet):
#         self.bouquet = bouquet




# #context manager

# #generator


# class ComputerConfig(DisplayMixin):

#     def __init__(self, name='noName', *args):
#         self.name = name
#         self.items = list(args)
#         should_have = ['MTB', 'VID', 'PRO', 'RAM', 'SSD']
#         for item in list(args):
#             if item.part_type in should_have:
#                 should_have.remove(item.part_type)
#             else:
#                 raise ValueError('you should have one of each component')
#         if should_have:
#             raise ValueError('you are missing : ' + str(should_have))
#         if len(args) < 5:
#             raise ValueError('the computer is missing components')
#         self.price = 0
#         for _ in list(args):
#             self.price += _.price


# config_list = []


# def log_configurator(fnc):
#     def inner_func(name, config_parts, values):
#         configure_computer = fnc(name, config_parts, values)
#         config_list.append(configure_computer.name)
#         return configure_computer

#     return inner_func

# # logging
# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG)


# # decorator
# @log_configurator
# def configure_computer(name, config_parts, values):
#     start = time.time()
#     proc = config_parts.pick_pro(values[0])
#     mtbd = config_parts.pick_mtb(values[1])
#     vide = config_parts.pick_vid(values[2])
#     rams = config_parts.pick_ram(values[3])
#     ssds = config_parts.pick_ssd(values[4])
#     end = time.time()
#     logger.info(f'configuration took {end - start} seconds')
#     return ComputerConfig(name, proc, mtbd, vide, rams, ssds)


# # context manager, decorator and generator
# @contextmanager
# def open_file(name):
#     f = open(name, 'w')
#     try:
#         yield f
#     finally:
#         f.close()

# def save_to_txt(txt='no text entered'):
#     with open_file('computer_history.txt') as f:
#         f.write(txt)
