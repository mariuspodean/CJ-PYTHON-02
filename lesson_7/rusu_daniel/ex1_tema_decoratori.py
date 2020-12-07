def uppercase(fnc):
    def wrapper(*args):
        return fnc(*args).upper()
    return wrapper

@uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet('WORLD'))