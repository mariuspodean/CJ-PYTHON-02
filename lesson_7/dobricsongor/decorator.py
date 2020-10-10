# Create a decorator called uppercase that will uppercase the result

def uppercase(fnc):
    
    def inner_func(given_text):
        return(fnc(given_text).upper())
    
    return inner_func
    

@uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet("World"))


#------------------------------------------------------------------------------

#Create a decorator called safe_divide that will output a message if the division cannot be performed, othervise it will return the result.

def safe_divide(fnc):

    def inner_func(first_num,second_num):
        if isinstance(first_num, (int,float)) and isinstance(second_num, (int,float)): 
            #if first_num % second_num == 0:
            print(f'The result of dividing the numbers {first_num} and {second_num} is: ',fnc(first_num,second_num))
        else:
            print(f'The operation divide of {first_num} and {second_num} cannot be done!') 

    return inner_func

@safe_divide
def divide(first_number, second_number):
    return first_number / second_number

divide(10.3, 2)
divide(18, 'a')

#----------------------------------------------------------------------------------

#Create a decorator called register that will update a list called print_registry with all the decorated functions names.

print_registry = []


def register(fnc):
    print_registry.append(fnc.__name__)
    return fnc


@register
def greet(name):
  return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

print('Decorated functions: ',print_registry)
#>>> ['greet', 'say_goodbye']