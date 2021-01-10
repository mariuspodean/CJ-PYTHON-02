def safe_divide(fnc):
    
    def wrapper(arg1,arg2):
         
        if(arg1 == 0):
         return print("Division cannot be performed")
        elif(arg2 == 0):
             return 0
        elif(arg1 >= 1 and arg2 >= 1):
            return arg1/arg2
        elif(arg1 < 0):
            return arg1 / arg2
        elif(arg2 <0):
            return arg1/ arg2
        elif(arg1 <0 and arg2 <0):
            return arg1/ arg2
    return wrapper
    


@safe_divide
def divide(first_number, second_number):
    return first_number / second_number

print(divide(-1,-2))
print(divide(-1,2))
print(divide(1,-2))
print(divide(0,2))
print(divide(1,0))
print(divide(3,4))