from functools import wraps
@register
print_registry=[]

def register(fnc):
    @wraps(fnc)
    def wrapper(fnc):
        return pretty_registry.append(fnc)
    return wrapper
    

@register
def greet(name):
    return "Greetings {}!".format(name)

@register
def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

print(print_registry)
