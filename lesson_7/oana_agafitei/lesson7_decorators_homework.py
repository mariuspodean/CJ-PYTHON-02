
'''def uppercase(name):

    def wrapper(input):

        res = name(input)
        modified = res.upper()

        return modified
    return wrapper

@uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet("World"))'''



def safe_divide(func):
    def inside(numerator, denominator):
        if denominator==0:
            print("Can't divide by 0")
            return
        func(numerator, denominator)
    return inside

@safe_divide
def divide(first_number, second_number):
    return first_number / second_number

print(divide(10, 0))



print_registry = []

def register(func):
    global print_registry
    print_registry.append(func.__name__)
    def inside(name):
        func(name)
    return inside

@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

print(print_registry)