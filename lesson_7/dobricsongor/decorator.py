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

    def inner_func(first,second):
        if first%second==0:
            print(f'The result of dividing the numbers {first} and {second} is: ',(int(first/second)))
        else:
            print('The operation divide cannot be done!') 
        return (fnc(first,second))

    return inner_func

@safe_divide
def divide(first_number, second_number):
    return first_number / second_number

(divide(10,2))

#----------------------------------------------------------------------------------

#Create a decorator called register that will update a list called print_registry with all the decorated functions names.

print_registry = []


#def register(fnc):



@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

print(print_registry)
#>>> ['greet', 'say_goodbye']