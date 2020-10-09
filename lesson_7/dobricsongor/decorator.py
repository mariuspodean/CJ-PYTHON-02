def uppercase(fnc):
    
    def inner_func(given_text):
        return(fnc(given_text).upper())
    
    return inner_func
    

@uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet("World"))


#------------------------------------------------------------------------------

def safe_divide(fnc):

    def inner_func(first,second):
        if first%second==0:
            print(f'The result of dividing the numbers {first} and {second} is: ',(int(first/second)))
        else:
            print('The operation divide cannot be done!') 
        return (fnc(first,second))

    return inner_func

@safe_divide
def divide(first_number, second_number):
    return first_number / second_number

(divide(10,2))

#----------------------------------------------------------------------------------