def uppercase (greet):
    
    def inner_func (message):
       return greet(message).upper()
    return inner_func

@uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet("World"))

