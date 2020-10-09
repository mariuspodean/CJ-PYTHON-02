def uppercase(fnc):
    
    def inner_func(given_text):
        return(fnc(given_text).upper())
    return inner_func
    

@uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet("World"))

