def uppercase_decorator(function):
        def inner_function(arg):
            func = function(arg)
            uppercase = func.upper()
            return uppercase
        return inner_function

@uppercase_decorator
def greet1(name):
    return "Greetings {}!".format(name)
print (greet1("World"))         



first_number = input('First number:')
second_number = input('Second number:')

def safe_divide (function):
    def inner_func(first, second):
        if second == 0:
            print("The division cannot be performed")
        else:
            result = function(first, second) 
            print("The division result is: {}".format(result))
    return inner_func

@ safe_divide
def divide(first_number, second_number):
    return (first_number / second_number)

divide(int(first_number), int(second_number))



print_registry = []
def register (function):
    def inner_functions(name):
        print(function(name))
        print_registry.append(function.__name__)
        return

    return inner_functions

@register
def greet(name):
    return "Greetings {}!".format(name)
    
@register
def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

greet("greet")
say_hello("say_hello")
say_goodbye("say_goodbye")

print(print_registry)