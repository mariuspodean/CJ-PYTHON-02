def safe_divide(divide):
    def safe_divide_inner(first_number, second_number):
        if second_number == 0:
            print("Division cannot be performed")
            return
        return divide(first_number, second_number)
    return safe_divide_inner


@safe_divide
def divide(first_number, second_number):
    return first_number/second_number

print(divide(9,3))