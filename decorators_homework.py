
# create a decorator called uppercase that will uppercase the result

def uppercase(func):

    def inner_up(msg):
        print('Message before upper: ', func(msg))
        print('Message after upper: ', func(msg).upper())
    return inner_up


@uppercase
def greet(name):
    return "Greetings {}!".format(name)


greet('World')
greet('Eva')