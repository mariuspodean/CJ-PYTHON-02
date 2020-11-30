from contextlib import contextmanager

class JustSomeExceptions:

    def __init__(self):
        print('init')

    def __enter__(self):
        print('enter')

    def __exit__(self, type, value, traceback):
        print(f'{type}, {value}, {traceback}')
        
        if(type == KeyError):
            print(f'Handled KeyError exception for key: {value}')
            return True
        if(type == IndexError):
            print(f'Handled IndexError exception: {value}')
            return True

my_dictionary = {"first_key":1, "second_key":2, "third_key": 3}
my_list = [1, 2, 3, 4]
with JustSomeExceptions() as some_exceptions:
    print("my code")
    print(my_dictionary["first_key"])
    print (my_list[1])
    #print (my_dictionary["five_key"])
    print (my_list[5])


print('\n')

@contextmanager
def just_some_exceptions():
    print("Execute just_some_exceptions function")
    try:
        yield 
    except KeyError:
        print('Handled KeyError exception')
    except IndexError:
        print('Handled IndexError exception')
    finally:
        print('finally')

with just_some_exceptions() as some_exceptions2:
    print("my second code")
    print (my_dictionary["first_key"])
    print (my_list[5])



