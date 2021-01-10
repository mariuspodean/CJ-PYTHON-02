from application import Person
from application import Kid
from application import Teacher
from application import Group
from application import Menu
from application import Kindergarten
from application import FileHandler
from application import menu_daily_generator
from application import list_menu_archive
from application import PrettyPrinter
from application import PrintGroup

person1 = Person('Siriciuc Anisia Maria', 'F', '03-07-2018', '074012314')
print(person1)
year, month = person1.get_age()

kid1 = Kid('Siriciuc Anisia', 'F', '06-07-2018', '0755955363',
           'Siriciuc Alexandra')
kid2 = Kid('Chelaru Calin', 'M', '26-05-2018', '0723755367', 'Chelaru Monica')
kid3 = Kid('Chelaru Anais', 'F', '27-08-2015', '0723456789', 'Chelaru MOnica')
kid4 = Kid('Franciuc Alin', 'M', '03-06-2017', '07209876', 'Franciuc Alina')
kid5 = Kid('Manta Evelina', 'F', '27-03-2016', '0734567890', 'Manta Madalina')
kid6 = Kid('Iacob Maya', 'F', '13-01-2016', '0745678901', 'Iacob Marius')

print(kid1)

if kid1 > kid2:
    print(f'Kid {kid1.get_name()} is greater than Kid {kid2.get_name()}')
else:
    print(f'Kid {kid2.get_name()} is greater than Kid {kid1.get_name()}')

teacher1 = Teacher('Tatiana', 'F', '10-02-1986', '074012314', 750)
teacher2 = Teacher('Gaby', 'F', '13-02-1987', '0740434480', 500)
teacher3 = Teacher('Cristina', 'F', '30-07-1986', '0721345678', 750)
teacher4 = Teacher('Paula', 'F', '10-03-1982', '0745678901', 700)

print(teacher1)

print(
    f'For the Teacher {teacher1.get_name()} the annual salary is {teacher1.get_annual_salary(teacher1.get_salary())}'
)

menu_dict1 = {
    'Monday': {
        'breakfast': ['corn flakes', 'full cream milk'],
        'lunch':
        ['rise with fish', 'mix beans and mushroom', 'radish and carrot soup'],
        'snack': ['fresh fruits']
    },
    'Tuesday': {
        'breakfast': ['chicken sausage sandwich', 'fresh fruits'],
        'lunch': [
            'beef and tomato bolognaise with wholemeal pasta',
            'mixed fresh vegetables'
        ],
        'snack': ['apricots pie']
    },
    'Wednesday': {
        'breakfast': ['hard boiled egg', 'toast or teacake'],
        'lunch': ['fish with spinach', 'chicken soup'],
        'snack': ['walnut biscuits']
    },
    'Thurday': {
        'breakfast': ['bread with peanut butter', 'full cream milk'],
        'lunch': ['chicken sandwich', 'cream corn', 'cucumber salad'],
        'snack': ['vanilla croissant']
    },
    'Friday': {
        'breakfast': ['bread with cheese and chicken'],
        'lunch': ['beef cottage pie with mashed potato', 'cabbage salad'],
        'snack': ['chicken sandwitch']
    }
}

menu_dict2 = {
    'Monday': {
        'breakfast': [
            'mini mushroom omelettes or breakfast cups',
            'strawberries and banana slices'
        ],
        'lunch': [
            'cream of parsnip and carrot soup',
            'raw vegetables (carrots, celery sticks, red pepper slices) with salad dressing for dipping'
        ],
        'snack': ['apple slices with nut butter or cheddar cheese']
    },
    'Tuesday': {
        'breakfast': ['oatmeal pancakes with apple sauce', 'milk'],
        'lunch': [
            'tuna grilled cheese or mini sandwiches on multigrain bread or whole wheat crackers',
            'Cucumber slices with dip'
        ],
        'snack': ['corn Muffin, orange juice']
    },
    'Wednesday': {
        'breakfast': ['donuts', 'banana', 'milk'],
        'lunch': ['cheese Lasagna', 'chicken soup'],
        'snack': ['apple muffin']
    },
    'Thursday': {
        'breakfast': ['banana bread', 'orange juice'],
        'lunch': ['bologna & cheese sandwich', 'vegetable soup'],
        'snack': [' biscuits', 'peaches']
    },
    'Friday': {
        'breakfast': ['pancakes', 'pears'],
        'lunch': ['baked potato with cheese, broccoli'],
        'snack': [' waffles']
    }
}

menu1 = Menu('16-11-2020', 13, menu_dict1)
menu2 = Menu('23-11-2020', 15, menu_dict2)
menu1.print_file()

menu_daily = menu_daily_generator(menu2)
daily_key, daily_value = next(menu_daily)
print(daily_key, daily_value)
daily_key, daily_value = next(menu_daily)
print(daily_key, daily_value)

baby_group = Group(Kindergarten.baby_group_name, teacher1)
first_group = Group(Kindergarten.first_group_name, teacher2)
second_group = Group(Kindergarten.second_group_name, teacher3)
third_group = Group(Kindergarten.third_group_name, teacher4)

kitty_kindergarten = Kindergarten('Kitty')

kitty_kindergarten.add_teacher(teacher1)
kitty_kindergarten.add_teacher(teacher2)
kitty_kindergarten.add_teacher(teacher3)
kitty_kindergarten.add_teacher(teacher4)

print(kitty_kindergarten._teacher_list)

kitty_kindergarten.add_group(baby_group)
kitty_kindergarten.add_group(first_group)
kitty_kindergarten.add_group(second_group)
kitty_kindergarten.add_group(third_group)

kitty_kindergarten.add_menu(menu1)
kitty_kindergarten.add_menu(menu2)
kitty_kindergarten.remove_menu(menu1)
print(list_menu_archive)

kitty_kindergarten.register_kid(kid1)
kitty_kindergarten.register_kid(kid2)
kitty_kindergarten.register_kid(kid3)
kitty_kindergarten.register_kid(kid4)
kitty_kindergarten.register_kid(kid5)
kitty_kindergarten.register_kid(kid6)

print(kitty_kindergarten._group_dict)
print(kitty_kindergarten._group_dict[Kindergarten.baby_group_name])
print(kitty_kindergarten._group_dict[Kindergarten.first_group_name])
print(kitty_kindergarten._group_dict[Kindergarten.second_group_name])
print(kitty_kindergarten._group_dict[Kindergarten.third_group_name])

group = kitty_kindergarten.get_group_by_name(Kindergarten.second_group_name)
print_group = PrintGroup(group.get_name(), group.get_teacher(),
                         group.get_kids_list())
print_group.pretty_printer()
