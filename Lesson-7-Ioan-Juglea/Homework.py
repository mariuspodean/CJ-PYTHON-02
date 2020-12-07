def uppercase(func):
    def inner_func(name):
        return func(name).upper()
    return inner_func


@uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet("World"))

def safe_divide(func):
    def inner_func(first_number, second_number):
        if second_number == 0:
            return "The division cannot be performed"
        else:
            return func(first_number, second_number)
    return inner_func

@safe_divide
def divide(first_number, second_number):
    return first_number / second_number

print(divide(8, 0))

print_registry = []

def register(func):
    print_registry.append(func.__name__)
    return func

@register
def greet_(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

print(print_registry)