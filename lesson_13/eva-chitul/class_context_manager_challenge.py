
class JustSomeExceptions:

    def __enter__(self):
        print('Looking for exceptions with a Class')
        return 'Here we go again'

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is IndexError:
            print('Houston, we have an Index problem!')
            return True
        elif exc_type is KeyError:
            print('Key error alert on deck!')
            return True


with JustSomeExceptions() as first_exception:
    print(first_exception)

    list_example = [1, 2, 3, (4, 5, 6), 'seven', 'eight']

    print(list_example[3])
    print(list_example[50])

with JustSomeExceptions() as second_exception:
    print(second_exception)

    dict_example = {'Chess': 'Queen', 'Tennis': 'Ball', 'Music': 'Instrument'}

    print(dict_example['Chess'])
    print(dict_example['Marathon'])

with JustSomeExceptions() as unknown_exception:
    print(unknown_exception)
    divide = 100/0
    print('Did we miss the error?')

