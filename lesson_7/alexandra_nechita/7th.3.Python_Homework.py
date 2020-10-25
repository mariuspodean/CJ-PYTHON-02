print_registry = []

def register (func):
    print_registry.append (func.__name__)
    def register_inner(message):
      print ('I am a useless function')
    return register_inner


def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


@register
def greet(name):
    return "Greetings {}!".format(name)


print (print_registry)
        