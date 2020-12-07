Let’s practise¶

    Given the following function:

def greet(name):
    return "Greetings {}!".format(name)

Create a decorator called uppercase that will uppercase the result

@uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet("World"))
>>> "GREETINGS WORLD!"

    Given the following function:

def divide(first_number, second_number):
    return first_number / second_number

Create a decorator called safe_divide that will output a message if the division cannot be performed, othervise it will return the result.

    Given a set of print methods:

print_registry = []


def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


def say_goodbye(name):
    return "Goodbye {}!".format(name)

Create a decorator called register that will update a list called print_registry with all the decorated functions names.

print_registry = []

@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

print(print_registry)
>>> ['greet', 'say_goodbye']
et’s practise¶

    Given the following function:

def greet(name):
    return "Greetings {}!".format(name)

Create a decorator called uppercase that will uppercase the result

@uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet("World"))
>>> "GREETINGS WORLD!"

    Given the following function:

def divide(first_number, second_number):
    return first_number / second_number

Create a decorator called safe_divide that will output a message if the division cannot be performed, othervise it will return the result.

    Given a set of print methods:

print_registry = []


def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


def say_goodbye(name):
    return "Goodbye {}!".format(name)

Create a decorator called register that will update a list called print_registry with all the decorated functions names.

print_registry = []

@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

print(print_registry)
>>> ['greet', 'say_goodbye']
